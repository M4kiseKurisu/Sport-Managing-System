<template>
    <!-- <div class="background">
        <div class="leftLayout"> -->
    <div class="logo">
        <div class="logo1"></div>
        <div class="logo2">Exercise.</div>
    </div>
    <div class="index active" ref="defaultIndex">
        <div class="icon1"></div>
        <div class="indexContent">个人信息</div>
    </div>
    <div class="index">
        <div class="icon2"></div>
        <div class="indexContent">活动管理</div>
    </div>
    <!-- </div>
    </div> -->
</template>

<script>
export default {
    mounted() {
    }
}
</script>

<style scoped>
.background {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    display: flex;
}

.leftLayout {
    float: left;
    display: block;
    height: 100%;
    width: 17%;
    position: fixed;
    background: linear-gradient(220.55deg, #5D85A6 0%, #0E2C5E 100%);
}

.logo {
    display: block;
    height: 100px;
    width: 100%;
    background-color: #5D85A6;
    object-fit: cover;
    overflow: hidden;
}

.logo1 {
    display: block;
    float: left;
    margin-top: 5px;
    height: 80%;
    margin-left: 10%;
    width: 30%;
    background: url(../images/logo.png) no-repeat;
    background-position: center;
    background-size: 50% 40%;
    background-size: cover;
    background-size: contain;
}

.logo2 {
    display: inline-block;
    font-size: 27px;
    margin-top: 30px;
    width: 50%;
    color: white;
    font-weight: bold;
    font-style: italic;
    margin-left: 5%;
}

.index {
    height: 60px;
    width: 100%;
    line-height: 60px;
    overflow: hidden;
    background-color: rgb(14, 43, 93, 0.6);
}

.active {
    background-color: rgb(14, 43, 93);
}

.icon1 {
    float: left;
    margin-left: 30px;
    vertical-align: middle;
    height: 60px;
    width: 80px;
    background-image: url(../images/personalInformation.png);
    background-repeat: no-repeat;
    background-position: center;
}

.icon2 {
    float: left;
    margin-left: 30px;
    vertical-align: middle;
    height: 60px;
    width: 80px;
    background-image: url(../images/activityManager.png);
    background-repeat: no-repeat;
    background-position: center;
}

.indexContent {
    display: block;
    float: left;
    font-size: 16px;
    margin-left: 20px;
    color: white;
}
</style>