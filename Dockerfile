FROM node

WORKDIR /gitgud-san-benito

COPY . .

USER node
RUN npm install --global gulp -y

WORKDIR /gitgud-san-benito/front

CMD ["node", "start"]