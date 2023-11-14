<template>
    <div class="create" id="create">
        <div class="content" id="content">
            <div class="title">创建账号</div>
            <div class="back">
                <div class="text1">已经拥有一个账号：</div>
                <a href="javascript:;" class="text2" @click="input">去登录</a>
            </div>
            <div class="contentAll">
                <div class="contentBlock">
                    <div class="flex">
                        <div class="tips">账号</div>
                        <div class="error" ref="textError">不能为空！</div>
                    </div>
                    <input type="text" :class="'inputClass'" v-model="account" ref="text">
                </div>
                <div class="contentBlock">
                    <div class="flex">
                        <div class="tips">密码</div>
                        <div class="error" ref="pwdError">不能为空！</div>
                    </div>
                    <input type="password" :class="'inputClass'" v-model="password" ref="pwd">
                </div>
                <div class="contentBlock">
                    <div class="flex">
                        <div class="tips">真实姓名</div>
                        <div class="error" ref="realNameError">不能为空！</div>
                    </div>
                    <input type="text" :class="'inputClass'" v-model="name" ref="realName">
                </div>
                <div class="contentBlock">
                    <div class="flex">
                        <div class="tips">性别</div>
                        <div class="error" ref="genderError">不能为空！</div>
                    </div>
                    <input type="radio" id="male" name="gender" value="male" :class="'radioClass'" checked />
                    <label for="male">男</label>
                    <input type="radio" id="female" name="gender" value="female" :class="'radioClass'" />
                    <label for="female">女</label>
                </div>
                <div class="contentBlock">
                    <div class="flex">
                        <div class="tips">电话号码</div>
                        <div class="error" ref="telError">不能为空！</div>
                    </div>
                    <input type="tel" :class="'inputClass'" v-model="phone" ref="tel">
                </div>
                <div class="contentBlock">
                    <div class="flex">
                        <div class="tips">电子邮箱</div>
                        <div class="error" ref="emailError">不能为空！</div>
                    </div>
                    <input type="email" :class="'inputClass'" v-model="email" ref="email">
                </div>
                <a href="javascript:;" class="finishBtn" @click="createAccount">创建账号</a>
            </div>

        </div>
    </div>
</template>

<script>
export default {
    methods: {
        input() {
            this.onEvent("Input");
        },
        createAccount() {
            /*未填写报错*/
            this.$refs.textError.style.opacity = (this.account) ? '0' : '1'
            this.$refs.text.style.border = (this.account) ? '' : 'solid 1px red'
            this.$refs.pwdError.style.opacity = (this.password) ? '0' : '1'
            this.$refs.pwd.style.border = (this.password) ? '' : 'solid 1px red'
            this.$refs.realNameError.style.opacity = (this.name) ? '0' : '1'
            this.$refs.realName.style.border = (this.name) ? '' : 'solid 1px red'
            this.$refs.telError.style.opacity = (this.phone) ? '0' : '1'
            this.$refs.tel.style.border = (this.phone) ? '' : 'solid 1px red'
            this.$refs.emailError.style.opacity = (this.email) ? '0' : '1'
            this.$refs.email.style.border = (this.email) ? '' : 'solid 1px red'
            this.male = (document.getElementById("male").checked) ? 1 : 0
            this.female = (document.getElementById("female").checked) ? 1 : 0
            /*填写格式错误报错*/
            const phoneFlag1 = (this.phone.length == 11) ? 1 : 0
            const phoneFlag2 = (/\d*/.test(this.phone)) ? 1 : 0
            if ((phoneFlag1 == 0 || phoneFlag2 == 0) && this.phone) {
                console.log(phoneFlag2)
                this.$refs.telError.innerHTML = (phoneFlag1 == 0) ? "电话号码需要为11位！" : "电话号码需要为纯数字！"
                this.$refs.telError.style.opacity = '1'
            }

            const emailForm = new RegExp(/.{1,}@.{1,}(\..{1,}){1,}/);
            const emailFlag = (!emailForm.test(this.email) && this.email) ? 0 : 1
            if (emailFlag == 0) {
                this.$refs.emailError.innerHTML = "邮箱格式错误！"
                this.$refs.emailError.style.opacity = '1'
            }
        }
    },
    props: {
        onEvent: Function
    },
    data() {
        return {
            account: '',
            password: '',
            name: '',
            phone: '',
            email: '',
            male: '',
            female: ''
        }
    },
    components: {

    }
}
</script>

<style scoped>
.create {
    position: fixed;
    overflow: hidden;
    width: 600px;
    height: 690px;
    z-index: 10;
    border-radius: 30px;
    display: flex;
    justify-content: flex-start;
    /*box-shadow:  10px 14px 16px -5px gray;*/
    border-top-style: inset;
    border-right-style: outset;
    border-color: rgb(239, 239, 239, .7);
    /* box-shadow: 8px -5px 16px -5px #868484; */
    border-width: 10px;
    margin-bottom: 10px;
    margin-left: 10px;
}

.content {
    width: 100%;
    height: 100%;
    background-color: rgb(255, 255, 255, 0.9);
}

.title {
    text-align: center;
    margin-top: 35px;
    font-size: 30px;
    font-weight: bold;
    color: #000000;
    line-height: 1.2;
    /* color: #4300B1; */
    color: #4C83FF;
    font-family: Helvetica, 'Hiragino Sans GB', 'Microsoft Yahei', '微软雅黑', Arial, sans-serif;
    letter-spacing: 3px;
}

.back {
    margin-top: 15px;
    font-size: 20px;
    text-align: center;
}

.text1 {
    /* color: #4300B1; */
    color: #4C83FF;
    display: inline-block;
    margin-right: 3px;
    font-family: Helvetica, 'Hiragino Sans GB', 'Microsoft Yahei', '微软雅黑', Arial, sans-serif;
}

.text2 {
    /* color: #A531DC;  */
    color: #2AFADF;
    text-decoration: underline;
    display: inline-block;
    margin-left: 3px;
    font-family: Helvetica, 'Hiragino Sans GB', 'Microsoft Yahei', '微软雅黑', Arial, sans-serif;
}

.text2:hover {
    background-color: white;
    color: rgb(19, 37, 196)
}

.contentAll {
    margin-top: 20px;
}

.contentBlock {
    text-align: center;
    margin-top: 8px;
}

.contentBlock .tips {
    text-align: left;
    margin-left: 120px;
}

.tips {
    color: #808080;
    font-size: 14px;
}

.inputClass {
    width: 360px;
    overflow: hidden;
    padding: 0 20px;
    height: 40px;
    line-height: 40px;
    border-radius: 4px;
    margin-top: 4px;
    font-size: 16px;
    background-color: #FEFEFE;
}

input {
    border: 1px solid #d0d0d0;
    background-color: transparent;
}

input:focus {
    outline-color: #4C83FF;
}

.radioClass {
    margin-top: 10px;
    margin-right: 30px;
    /* color: #4300B1; */
}

label {
    margin-right: 50px;
    font-size: 16px;
}

.finishBtn {
    width: 360px;
    display: block;
    text-align: center;
    line-height: 40px;
    margin: 35px auto;
    height: 40px;
    color: #FFFFFF;
    font-size: 16px;
    font-weight: bold;
    border-radius: 4px;
    position: relative;
    text-decoration: none;
}

.contentAll .finishBtn {
    /* background:linear-gradient(220.55deg, #A531DC 0%, #4300B1 100%); */
    background: linear-gradient(220.55deg, #2AFADF 0%, #4C83FF 100%);
    text-align: center;
}

.radioClass[type="radio"] {
    appearance: none;

    border-radius: 20%;
    width: 16px;
    height: 16px;

    border: 2px solid #999;
    transition: 0.2s all linear;
    margin-right: 10px;

    position: relative;
    top: 4px;
}

.radioClass[type="radio"]:checked {
    border: 6px solid #4C83FF;
}

.error {
    font-size: 14px;
    color: red;
    margin-right: 120px;
    opacity: 0;
}

.flex {
    display: flex;
    justify-content: space-between;
}
</style>