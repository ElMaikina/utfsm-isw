
FROM node as web
USER root
WORKDIR /gitgud-san-benito/front

COPY ./package*.json ./
COPY ./package-lock*.json ./
WORKDIR /gitgud-san-benito/front/public
COPY ./index*.html ./
WORKDIR /gitgud-san-benito/front/src
COPY ./src/* ./
RUN npm install --global gulp -y
RUN npm ci --omit=dev

COPY . ./
RUN npm run build 
# release step

EXPOSE 8080 3000


CMD ["npm", "start"]

