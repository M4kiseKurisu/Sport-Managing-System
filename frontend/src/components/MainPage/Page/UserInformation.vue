<template>
  <el-row>
    <el-col :span="8">
      <!-- 头像组件 -->

      <div class="avatarDiv">
        <el-avatar v-if="this.picture === 'http://127.0.0.1:8000null'" :size="150" shape="circle"
          :src="'./src/images/emptyAvatar.png'"></el-avatar>
        <el-avatar v-else :size="150" shape="circle" :src="picture"></el-avatar>
      </div>

      <!-- 个人账号 -->

      <div class="nameDiv">
        <div>你好啊：</div>
        <div>{{ name }}</div>
        <div class="genderSign">
          <el-icon v-if="this.gender === '女'">
            <Female />
          </el-icon>
          <el-icon v-else>
            <Male />
          </el-icon>
        </div>
      </div>

      <!-- 个人签名 -->

      <div class="signDiv">
        <div>{{ sign }}</div>
      </div>

      <el-divider />

      <!-- 个人数据 -->

      <div class="statistic">
        <el-row>
          <el-col :span="8">
            <el-statistic title="好友" :value="this.friend" />
          </el-col>
          <el-col :span="8">
            <el-statistic title="已参加活动" :value="this.activity" />
          </el-col>
          <el-col :span="8">
            <el-statistic title="已参加团体" :value="this.group" />
          </el-col>
        </el-row>
      </div>

      <el-divider />

      <!-- 其他个人信息 -->

      <div class="information">
        <div class="informationRow">其他个人信息：</div>

        <div class="informationRow">
          <div class="icon">
            <el-icon>
              <User />
            </el-icon>
          </div>

          <div class="text">年龄：{{ age }}岁</div>
        </div>

        <div class="informationRow">
          <div class="icon">
            <el-icon>
              <Phone />
            </el-icon>
          </div>

          <div class="text">电话号码：{{ phone }}</div>
        </div>

        <div class="informationRow">
          <div class="icon">
            <el-icon>
              <Message />
            </el-icon>
          </div>

          <div class="text">个人邮箱：{{ email }}</div>
        </div>
      </div>

      <!-- 更改个人信息按钮 -->
      <div class="changeButton">
        <div class="button">
          <el-upload v-model:file-list="this.fileList" :limit="1" :show-file-list="false" :auto-upload="false" action="#">
            <el-button type="primary" plain>选择头像</el-button>
          </el-upload>
        </div>

        <div class="button">
          <el-button type="primary" @click="upload">点击上传</el-button>
        </div>

        <ChangeUserInformation />
      </div>
    </el-col>

    <el-col :span="8">
      <!-- 活动饼状图 -->
      <div class="tipContainer">
        <div class="chartTip">当前已参加活动</div>
      </div>

      <div class="pieChart">
        <Echart />
      </div>
    </el-col>

    <el-col :span="8">
      <!-- 团体饼状图 -->
      <div class="tipContainer">
        <div class="chartTip">当前已参加团体</div>
      </div>

      <div class="pieChart">
        <Echart2 />
      </div>
    </el-col>
  </el-row>
</template>

<script>
import Echart from "../Components/Echart.vue";
import Echart2 from "../Components/Echart2.vue";
import ChangeUserInformation from "../Components/ChangeUserInformation.vue";
import axios from "axios";
import { Female, Male, User, Phone, Message } from "@element-plus/icons-vue";
export default {
  data() {
    return {
      fileList: [],
      name: "",
      age: "",
      gender: "",
      phone: "",
      email: "",
      sign: "这个人很懒，还没有留下任何签名哦~",
      picture: "",
      activity: "",
      friend: "",
      group: "",

      dataList: [],
    };
  },
  components: {
    Echart,
    Echart2,
    ChangeUserInformation,
    Female,
    Male,
    User,
    Phone,
    Message,
  },
  created() {
    axios({
      method: "GET",
      url: "http://127.0.0.1:8000/api/user/information",
      params: {
        uid: JSON.parse(sessionStorage.getItem("uid")),
      },
    }).then((result) => {
      console.log(result);
      if (result.data.status) {
        this.name = result.data.info.name;
        this.age = result.data.info.age;
        this.gender = result.data.info.gender;
        this.phone = result.data.info.phone;
        this.email = result.data.info.email;
        this.sign = result.data.info.signature;
        this.picture = "http://127.0.0.1:8000" + result.data.info.picture;
        this.activity = result.data.info.activity;
        this.friend = result.data.info.friend;
        this.group = result.data.info.group;
        console.log(this.picture);
      }
    });
  },
  methods: {
    show() {
      console.log(this.fileList);
    },
    beforeUpload(file) {
      let isPic = file.type === "image/jpeg" || file.type === "image/png";
      if (!isPic) {
        this.$message({
          showClose: true,
          message: "只能上传JPG/PNG形式的图片",
          type: "error",
        });
      }
      return isPic;
    },
    upload() {
      const file = this.fileList[0].raw;
      const uid = sessionStorage.getItem("uid");
      const data = new FormData();

      data.append("uid", uid);
      data.append("picture", file);

      console.log(file);

      axios.post("http://127.0.0.1:8000/api/user/modify/pic", data);
    },
    uploadFile(file) {
      let picInput = null;
      picInput.append("uid", JSON.parse(sessionStorage.getItem("uid")));
      picInput.append("picture", file.raw);

      console.log(file.raw);

      axios({
        method: "POST",
        url: "http://127.0.0.1:8000/api/user/modify/pic",
        data: picInput,
      }).then((result) => {
        if (result.data.status) {
          this.$message({
            showClose: true,
            message: result.data.msg,
            type: "success",
          });
        } else {
          this.$message({
            showClose: true,
            message: result.data.msg,
            type: "error",
          });
        }
      });
    },
  },
};
</script>

<style scoped>
.el-col {
  text-align: center;
}

.avatarDiv {
  display: flex;
  justify-content: center;
  padding-top: 20px;
  margin-top: 50px;
}

.nameDiv {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 20px;
}

.genderSign {
  margin-top: 2px;
  margin-left: 6px;
  height: 60%;
}

.signDiv {
  margin-top: 10px;
  display: flex;
  justify-content: center;
  font-size: 14px;
  color: gray;
}

.pieChart {
  display: flex;
  justify-content: center;
}

.information {
  font-size: 16px;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
}

.informationRow {
  display: flex;
  margin-bottom: 10px;
  margin-left: 16px;
}

.text {
  font-size: 16px;
  margin-left: 6px;
}

.icon {
  vertical-align: center;
  padding-top: 3px;
}

.button {
  margin-right: 20px;
}

.changeButton {
  margin-top: 16px;
  display: flex;
  justify-content: flex-end;
  margin-right: 20px;
}

.tipContainer {
  margin-top: 150px;
  display: flex;
}

.chartTip {
  margin-left: 8%;
  font-size: 18px;
}
</style>
  