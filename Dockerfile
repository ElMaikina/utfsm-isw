FROM node

WORKDIR /gitgud-san-benito



USER root
WORKDIR /gitgud-san-benito/front

COPY /gitgud-san-benito/front/package*.json ./
COPY /gitgud-san-benito/front/package-lock*.json ./
WORKDIR /gitgud-san-benito/front/public
COPY /gitgud-san-benito/front/public/index*.html ./
WORKDIR /gitgud-san-benito/front/src
COPY /gitgud-san-benito/front/src/* ./
RUN npm install --global gulp -y
RUN npm ci --omit=dev

COPY . ./
RUN npm run build
# release step
EXPOSE 3000

EXPOSE 8080

CMD ["npm", "start"]