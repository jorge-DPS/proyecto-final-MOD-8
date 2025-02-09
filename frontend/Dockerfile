# Usa Node.js 22.13 como imagen base
FROM node:22.13.0

# Establece el directorio de trabajo
WORKDIR /app

# Copia package.json y package-lock.json para instalar dependencias
COPY package.json package-lock.json ./

RUN npm install

# Copia el código fuente
COPY . .

# Expone el puerto de desarrollo de Vite
EXPOSE 5173

# Comando para iniciar Vue con Vite
CMD ["npm", "run", "dev"]