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
                <input type="text" placeholder="账号输入" :class="'logInput'" v-model="account">
                <div class="error" ref="textError">不能为空!</div>
                <input type="password" placeholder="密码输入" :class="'logInput'" v-model="password">
                <div class="error" ref="pwdError">不能为空!</div>
                <a href="javascript:;" class="logBtn" @click="login">登录</a>
                <a href="javascript:;" class="create" @click="create">创建账号</a>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            account: '',
            password: ''
        }
    },
    methods: {
        create() {
            this.onEvent("Create");
        },
        login() {
            this.$refs.textError.style.opacity = (this.account) ? '0' : '1'
            this.$refs.pwdError.style.opacity = (this.password) ? '0' : '1'
        }
    },
    props: {
        onEvent: Function
    }
}
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
    /* background:linear-gradient(220.55deg, #A531DC 0%, #4300B1 100%); */
    /*background: linear-gradient(220.55deg, #FFE70B 0%, #27B643 100%);*/
    background: linear-gradient(220.55deg, #2AFADF 0%, #4C83FF 100%);
}

.logopic {
    background-image: url(../images/logo.png);
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
    color: #FFFFFF;
    font-family: 'Courier New', Courier, monospace
}

.input {
    width: 40%;
    height: 100%;
    background-color: #FEFEFE;
    opacity: 0.9;
}

.title {
    text-align: center;
    margin-top: 60px;
    font-size: 30px;
    font-weight: bold;
    /* color: #4300B1; */
    color: #4C83FF;
    line-height: 1.2;
    letter-spacing: 3px;
    font-family: Helvetica, 'Hiragino Sans GB', 'Microsoft Yahei', '微软雅黑', Arial, sans-serif;

}

.shape {
    width: 200px;
    height: 50px;
    border-radius: 0 25px 25px 0;
    /* background:linear-gradient(220.55deg, #A531DC 0%, #4300B1 100%); */
    /*background: linear-gradient(220.55deg, #FFE70B 0%, #29e04e 100%);*/
    background: linear-gradient(220.55deg, #2AFADF 0%, #4C83FF 100%);
}

.logContent {
    text-align: center;
    margin-top: 60px;
}

.logContent .logBtn {
    /* background:linear-gradient(220.55deg, #A531DC 0%, #4300B1 100%); */
    /*background: linear-gradient(220.55deg, #FFE70B 0%, #29e04e 100%);*/
    background: linear-gradient(220.55deg, #2AFADF 0%, #4C83FF 100%);
    text-align: center;
}

.logInput {
    display: block;
    overflow: hidden;
    padding: 0 60px;
    height: 48px;
    line-height: 48px;
    border-radius: 24px;
    font-size: 15px;
    margin: 0 auto 0px;
    background-color: #111111;
    box-shadow: 0px 3px 16px -5px #020202;
    font-weight: bold;
    letter-spacing: 0.7px;
    color: #FFFFFF;
}

input::placeholder {
    font-weight: bold;
    letter-spacing: 0.7px;
    color: #FFFFFF;
    font-family: Helvetica, 'Hiragino Sans GB', 'Microsoft Yahei', '微软雅黑', Arial, sans-serif;
}

input[type="password"]::-ms-reveal {
    display: none;
}

.logBtn {
    width: 200px;
    display: block;
    text-align: left;
    line-height: 48px;
    margin: 30px auto;
    height: 48px;
    color: #FFFFFF;
    font-size: 26px;
    letter-spacing: 6px;
    font-weight: bold;
    border-radius: 24px;
    position: relative;
    font-family: Helvetica, 'Hiragino Sans GB', 'Microsoft Yahei', '微软雅黑', Arial, sans-serif;
}

.create {
    margin-top: 5px;
    /* color: #9932CC;  */
    color: #4C83FF;
    font-size: 15px;
    letter-spacing: 3px;
    /* border-bottom:1px solid #9932CC;  */
    border-bottom: 1px solid rgb(76, 131, 255, .7);
    display: inline-block;
    padding-bottom: 5px;
    font-family: Helvetica, 'Hiragino Sans GB', 'Microsoft Yahei', '微软雅黑', Arial, sans-serif;
}

.create:hover {
    background-color: white;
    color: rgb(24, 84, 223);
    font-weight: bold;
}

.logInput[type="text"] {
    background-image: url(../images/password2.png);
    background-repeat: no-repeat;
    background-position: left;
    background-position: 15px;
}

.logInput[type=password] {
    background-image: url(../images/password.png);
    background-repeat: no-repeat;
    background-position: left;
    background-position: 15px;
}

.error {
    margin-top: 5px;
    margin-bottom: 25px;
    margin-left: 200px;
    color: red;
    opacity: 0;

}
</style>