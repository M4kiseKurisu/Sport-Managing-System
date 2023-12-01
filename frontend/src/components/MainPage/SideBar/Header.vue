<template>
  <div class="header">
    <!-- 左侧logo -->
    <div class="picLocation">
      <img src="../../../images/logo.png" class="pic" />
    </div>

    <!-- 右侧内容 -->
    <div class="right">
      <!-- 头像 -->
      <div>
        <el-avatar :size="50" :src="picture || './src/images/emptyAvatar.png'" />
      </div>

      <!-- 账号 -->
      <div class="text">
        <div class="textStyle">{{ name }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import { color } from "echarts/core"
import axios from 'axios'
export default {
  data() {
    return {
      name: '',
      picture: '',
    };
  },
  methods: {},
  created() {
    axios({
      method: "GET",
      url: "http://127.0.0.1:8000/api/user/information",
      params: {
        uid: JSON.parse(sessionStorage.getItem("uid")),
      },
    }).then((result) => {
      if (result.data.status) {
        this.name = result.data.info.name;
        this.picture = "http://127.0.0.1:8000" + result.data.info.picture;
      }
    });
  }
};
</script>

<style scoped>
.header {
  height: 100%;
  display: flex;
  justify-content: space-between;
  background-color: #5d85a6;
}

.picLocation {
  height: 90%;
  width: 100px;
  margin-top: 6px;
}

.pic {
  background-repeat: no-repeat;
  background-position: center;
  object-fit: contain;
  width: 100%;
  height: 100%;
}

.right {
  margin-top: 6px;
  display: flex;
  flex-direction: row;
}

.text {
  display: flex;
  align-items: center;
  margin-left: 20px;
  margin-right: 20px;
}

.textStyle {
  font-size: 18px;
  color: white;
}
</style>