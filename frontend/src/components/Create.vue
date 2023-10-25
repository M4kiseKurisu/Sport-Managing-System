<template>
    <div class="create" id="create">
        <!-- <div class="custom-shape-divider-top-1698147972">
            <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
                <path d="M1200 0L0 0 892.25 114.72 1200 0z" class="shape-fill"></path>
            </svg>
        </div> -->
        <div class="content" id="content">
            <div class="title">创建账号</div>
            <div class="back">
                <div class="text1">已经拥有一个账号：</div>
                <a href="javascript:;" class="text2" @click="input">去登录</a>
            </div>
            <div class="contentAll">
                <div class="contentBlock">
                    <div class="tips">账号</div>
                    <input type="text" :class="'inputClass'" v-model="account">
                </div>
                <div class="contentBlock">
                    <div class="tips">密码</div>
                    <input type="password" :class="'inputClass'" v-model="password">
                </div>
                <div class="contentBlock">
                    <div class="tips">真实姓名</div>
                    <input type="text" :class="'inputClass'" v-model="name">
                </div>
                <div class="contentBlock">
                    <div class="tips">性别</div>
                    <input type="radio" id="male" name="gender" value="male" :class="'radioClass'" />
                    <label for="male">男</label>
                    <input type="radio" id="female" name="gender" value="female" :class="'radioClass'" />
                    <label for="female">女</label>
                </div>
                <div class="contentBlock">
                    <div class="tips">电话号码</div>
                    <input type="tel" :class="'inputClass'" v-model="phone">
                </div>
                <div class="contentBlock">
                    <div class="tips">电子邮箱</div>
                    <input type="email" :class="'inputClass'" v-model="email">
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
            email: ''
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
}

.contentAll .finishBtn {
    /* background:linear-gradient(220.55deg, #A531DC 0%, #4300B1 100%); */
    background: linear-gradient(220.55deg, #2AFADF 0%, #4C83FF 100%);
    text-align: center;
}

/* .custom-shape-divider-top-1698147972 {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    overflow: hidden;
    line-height: 0;
}

.custom-shape-divider-top-1698147972 svg {
    position: relative;
    display: block;
    width: calc(181% + 1.3px);
    height: 115px;
}

.custom-shape-divider-top-1698147972 .shape-fill {
    fill: #2AFADF;
} */
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
</style>