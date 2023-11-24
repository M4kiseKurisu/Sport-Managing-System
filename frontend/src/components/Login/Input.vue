<template>
  <div class="login" id="login">
    <div class="logo" id="logo">
      <div class="logopic"></div>
      <div class="tifo">Start Exercising.</div>
    </div>

    <div class="input" id="input">
      <div class="shape"></div>
      <div class="title">用户登录</div>
      <div class="logContent">
        <div class="account-box">
          <input
            type="text"
            placeholder="账号输入"
            :class="'logInput'"
            v-model="account"
          />
        </div>
        <div class="account-error" ref="accountError">账号不能为空</div>
        <div class="password-box">
          <input
            type="password"
            placeholder="密码输入"
            :class="'logInput'"
            v-model="password"
          />
        </div>
        <div class="password-error" ref="passwordError">密码不能为空</div>

        <a href="javascript:;" class="logBtn" @click="login">登录</a>
        <a href="javascript:;" class="create" @click="create">创建账号</a>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      account: "",
      password: "",
      // uid: "",
      // user_name: "",
    };
  },
  methods: {
    create() {
      this.onEvent("Create");
    },
    login() {
      this.$refs.accountError.style.opacity = this.account ? "0" : "1";
      this.$refs.passwordError.style.opacity = this.password ? "0" : "1";
      if (this.account && this.password) {
        axios({
          method: "GET",
          url: "http://127.0.0.1:8000/api/user/login",
          params: {
            account: this.account,
            password: this.password,
          },
        }).then((result) => {
          if (result.data.status) {
            this.$store.commit("userLogin", result.data);
            console.log(sessionStorage.getItem("uid"));
            this.$router.push({ path: "Page/User_Information" });
          } else {
            alert("账号或密码不正确");
          }
        });
      }
    },
  },
  props: {
    onEvent: Function,
  },
};
</script>

<style scoped>
.login {
  position: fixed;
  overflow: hidden;
  width: 1093px;
  height: 560px;
  z-index: 10;
  border-radius: 30px;
  display: flex;
  justify-content: flex-start;
}

.logo {
  width: 70%;
  height: 100%;
  background: linear-gradient(220.55deg, #0ddcc0 0%, #4c83ff 100%);
}

.logopic {
  background-image: url(../../images/logo.png);
  background-repeat: no-repeat;
  background-position: center;
  width: 100%;
  height: 100%;
  margin-top: -30px;
}

.tifo {
  margin-top: -70px;
  text-align: center;
  font-size: 20px;
  color: #ffffff;
  font-family: "Courier New", Courier, monospace;
}

.input {
  width: 40%;
  height: 100%;
  background-color: #fefefe;
  opacity: 0.9;
}

.title {
  text-align: center;
  margin-top: 60px;
  font-size: 30px;
  font-weight: bold;
  /* color: #4300B1; */
  color: #4c83ff;
  line-height: 1.2;
  letter-spacing: 3px;
  font-family: Helvetica, "Hiragino Sans GB", "Microsoft Yahei", "微软雅黑",
    Arial, sans-serif;
}

.shape {
  width: 200px;
  height: 50px;
  border-radius: 0 25px 25px 0;
  background: linear-gradient(220.55deg, #2afadf 0%, #4c83ff 100%);
}

.logContent {
  text-align: center;
  margin-top: 60px;
  padding: 10%;
  padding-top: 0px;
}

.logContent .logBtn {
  background: linear-gradient(220.55deg, #2afadf 0%, #4c83ff 100%);
  text-align: center;
}

.account-box,
.password-box {
  display: inline-block;
  border-bottom: 2px solid #111111;
}

.logInput {
  display: inline-block;
  padding: 0 20px;
  width: 180px;
  height: 48px;
  line-height: 48px;
  border: none;
  font-size: 18px;
  outline: none;
  font-weight: bold;
  background-color: transparent;
  color: #252525;
}

.password-error,
.account-error {
  text-align: right;
  padding: 25px;
  padding-top: 10px;
  color: red;
  opacity: 0;
}

.account-box::before {
  width: 25px;
  height: 25px;
  content: "";
  vertical-align: middle;
  display: inline-block;
  background-image: url("./src/images/account.png");
  background-size: cover;
}

.password-box::before {
  width: 25px;
  height: 25px;
  content: "";
  vertical-align: middle;
  display: inline-block;
  background-image: url("./src/images/password.png");
  background-size: cover;
}

input::placeholder {
  font-weight: bold;
  font-size: 16px;
  color: rgb(62, 62, 62, 0.7);
  font-family: Helvetica, "Hiragino Sans GB", "Microsoft Yahei", "微软雅黑",
    Arial, sans-serif;
}

.logBtn {
  width: 200px;
  display: block;
  text-align: left;
  line-height: 48px;
  margin: 20px auto;
  height: 48px;
  color: #ffffff;
  font-size: 26px;
  letter-spacing: 6px;
  font-weight: bold;
  border-radius: 24px;
  position: relative;
  font-family: Helvetica, "Hiragino Sans GB", "Microsoft Yahei", "微软雅黑",
    Arial, sans-serif;
  text-decoration: none;
}

.create {
  margin-top: 5px;
  /* color: #9932CC;  */
  color: #4c83ff;
  font-size: 15px;
  letter-spacing: 3px;
  /* border-bottom:1px solid #9932CC;  */
  border-bottom: 1px solid rgb(76, 131, 255, 0.7);
  display: inline-block;
  padding-bottom: 5px;
  font-family: Helvetica, "Hiragino Sans GB", "Microsoft Yahei", "微软雅黑",
    Arial, sans-serif;
  text-decoration: none;
}

.create:hover {
  background-color: white;
  color: rgb(24, 84, 223);
  font-weight: bold;
}

.error {
  margin-top: 5px;
  margin-bottom: 25px;
  margin-left: 200px;
  color: red;
  opacity: 0;
}
</style>