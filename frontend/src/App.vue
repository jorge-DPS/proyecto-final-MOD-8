<script setup>
import { ref, computed } from 'vue'

const contacts = ref([
  {
    id: 1,
    name: "Alice Johnson",
    email: "alice.johnson@example.com",
    address: "123 Maple Street",
    phone: "123-456-7890",
    country: "USA",
    city: "New York"
  },
  {
    id: 2,
    name: "Bob Smith",
    email: "bob.smith@example.com",
    address: "456 Oak Avenue",
    phone: "987-654-3210",
    country: "Canada",
    city: "Toronto"
  },
  {
    id: 3,
    name: "Carol White",
    email: "carol.white@example.com",
    address: "789 Pine Road",
    phone: "555-123-4567",
    country: "UK",
    city: "London"
  },
  {
    id: 4,
    name: "David Brown",
    email: "david.brown@example.com",
    address: "321 Elm Street",
    phone: "444-555-6666",
    country: "Australia",
    city: "Sydney"
  },
  {
    id: 5,
    name: "Emily Davis",
    email: "emily.davis@example.com",
    address: "654 Spruce Lane",
    phone: "333-444-5555",
    country: "USA",
    city: "Los Angeles"
  }
])

const searchTerm = ref('')
const editingContact = ref(null)
const showForm = ref(false)
const formRef = ref(null)
const newContact = ref({
  name: '',
  email: '',
  address: '',
  phone: '',
  country: '',
  city: ''
})

const filteredContacts = computed(() => {
  const search = searchTerm.value.toLowerCase()
  return contacts.value.filter(contact => 
    contact.name.toLowerCase().includes(search) ||
    contact.email.toLowerCase().includes(search)
  )
})

const addContact = () => {
  const contact = {
    ...newContact.value,
    id: contacts.value.length + 1
  }
  contacts.value.push(contact)
  resetForm()
}

const deleteContact = (id) => {
  if (confirm('¿Estás seguro de que deseas eliminar este contacto?')) {
    contacts.value = contacts.value.filter(contact => contact.id !== id)
  }
}

const startEdit = (contact) => {
  editingContact.value = { ...contact }
  showForm.value = true
  
  setTimeout(() => {
    formRef.value?.scrollIntoView({ 
      behavior: 'smooth',
      block: 'start'
    })
  }, 100)
}

const saveEdit = () => {
  const index = contacts.value.findIndex(c => c.id === editingContact.value.id)
  contacts.value[index] = { ...editingContact.value }
  resetForm()
}

const resetForm = () => {
  editingContact.value = null
  showForm.value = false
  newContact.value = {
    name: '',
    email: '',
    address: '',
    phone: '',
    country: '',
    city: ''
  }
}
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Header -->
    <header class="bg-white shadow">
      <div class="container mx-auto px-4 py-6">
        <h1 class="text-3xl font-bold text-gray-800">
          Gestión de Contactos
        </h1>
      </div>
    </header>

    <main class="container mx-auto px-4 py-8">
      <!-- Search and Add Contact Row -->
      <div class="flex flex-col md:flex-row justify-between items-center gap-4 mb-8">
        <div class="relative w-full md:w-96">
          <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
          </div>
          <input
            v-model="searchTerm"
            type="text"
            placeholder="Buscar por nombre o email..."
            class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          >
        </div>
        <button
          v-if="!showForm"
          @click="showForm = true"
          class="w-full md:w-auto bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition-colors duration-200 flex items-center justify-center gap-2"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
          </svg>
          Nuevo Contacto
        </button>
      </div>

      <!-- Form Section -->
      <div 
        v-if="showForm" 
        class="bg-white rounded-lg shadow-lg mb-8 transition-all duration-300"
        ref="formRef"
      >
        <div class="p-6">
          <h2 class="text-2xl font-semibold text-gray-800 mb-6">
            {{ editingContact ? 'Editar Contacto' : 'Nuevo Contacto' }}
          </h2>
          <form @submit.prevent="editingContact ? saveEdit() : addContact()" class="space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div class="space-y-2">
                <label class="text-sm font-medium text-gray-700">Nombre</label>
                <input
                  v-model="(editingContact || newContact).name"
                  class="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  required
                >
              </div>
              <div class="space-y-2">
                <label class="text-sm font-medium text-gray-700">Email</label>
                <input
                  v-model="(editingContact || newContact).email"
                  type="email"
                  class="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  required
                >
              </div>
              <div class="space-y-2">
                <label class="text-sm font-medium text-gray-700">Teléfono</label>
                <input
                  v-model="(editingContact || newContact).phone"
                  class="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  required
                >
              </div>
              <div class="space-y-2">
                <label class="text-sm font-medium text-gray-700">Dirección</label>
                <input
                  v-model="(editingContact || newContact).address"
                  class="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  required
                >
              </div>
              <div class="space-y-2">
                <label class="text-sm font-medium text-gray-700">País</label>
                <input
                  v-model="(editingContact || newContact).country"
                  class="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  required
                >
              </div>
              <div class="space-y-2">
                <label class="text-sm font-medium text-gray-700">Ciudad</label>
                <input
                  v-model="(editingContact || newContact).city"
                  class="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  required
                >
              </div>
            </div>
            <div class="flex gap-4">
              <button
                type="submit"
                class="flex-1 bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition-colors duration-200"
              >
                {{ editingContact ? 'Guardar Cambios' : 'Agregar Contacto' }}
              </button>
              <button
                type="button"
                @click="resetForm"
                class="flex-1 bg-gray-500 text-white px-6 py-2 rounded-lg hover:bg-gray-600 transition-colors duration-200"
              >
                Cancelar
              </button>
            </div>
          </form>
        </div>
      </div>

      <!-- Contacts Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="contact in filteredContacts"
          :key="contact.id"
          class="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200"
        >
          <div class="p-6">
            <div class="flex justify-between items-start mb-4">
              <div>
                <h3 class="text-xl font-semibold text-gray-800 mb-2">{{ contact.name }}</h3>
                <div class="space-y-1">
                  <p class="text-gray-600 flex items-center gap-2">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                    </svg>
                    {{ contact.email }}
                  </p>
                  <p class="text-gray-600 flex items-center gap-2">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                    </svg>
                    {{ contact.phone }}
                  </p>
                  <p class="text-gray-600 flex items-center gap-2">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                    </svg>
                    {{ contact.address }}
                  </p>
                  <p class="text-gray-600 flex items-center gap-2">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064" />
                    </svg>
                    {{ contact.city }}, {{ contact.country }}
                  </p>
                </div>
              </div>
            </div>
            <div class="flex gap-2">
              <button
                @click="startEdit(contact)"
                class="flex-1 bg-yellow-500 text-white px-4 py-2 rounded-lg hover:bg-yellow-600 transition-colors duration-200 flex items-center justify-center gap-2"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                </svg>
                Editar
              </button>
              <button
                @click="deleteContact(contact.id)"
                class="flex-1 bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition-colors duration-200 flex items-center justify-center gap-2"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                </svg>
                Eliminar
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <div v-if="filteredContacts.length === 0" class="text-center py-12">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-16 w-16 mx-auto text-gray-400 mb-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
        </svg>
        <h3 class="text-xl font-medium text-gray-900 mb-1">No se encontraron contactos</h3>
        <p class="text-gray-500">No hay contactos que coincidan con tu búsqueda.</p>
      </div>
    </main>
  </div>
</template>

<style>
/* Transition animations */
.v-enter-active,
.v-leave-active {
  transition: opacity 0.3s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>