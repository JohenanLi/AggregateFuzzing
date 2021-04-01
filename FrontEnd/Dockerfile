FROM node	

ADD . /app	

WORKDIR /app	
# # 设置淘宝npm镜像
# RUN npm install -g cnpm --registry=https://registry.npm.taobao.org
# # 安装依赖
# RUN cnpm install
RUN npm install
CMD ["npm", "run", "serve"]	