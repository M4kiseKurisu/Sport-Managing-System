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
    height: 12%;
    width: 100%;
    background-color: #5D85A6;
    object-fit: cover;
    overflow: hidden;
}

.logo1 {
    display: block;
    float: left;
    margin-left: 30px;
    margin-top: 5px;
    height: 80%;
    width: 80px;
    background-image: url(../images/logo.png);
    background-repeat: no-repeat;
    background-position: center;
    object-fit: cover;
    background-size: 100% 100%;
}

.logo2 {
    display: block;
    float: left;
    font-size: 27px;
    margin-top: 30px;
    margin-left: 20px;
    color: white;
    font-weight: bold;
    font-style: italic;
}

.index {
    display: block;
    height: 8%;
    width: 100%;
    overflow: hidden;
    background-color: rgb(14, 43, 93, 0.6);
}

.active {
    background-color: rgb(14, 43, 93);
}

.icon1 {
    display: block;
    float: left;
    margin-left: 30px;
    margin-top: 7px;
    height: 80%;
    width: 80px;
    background-image: url(../images/personalInformation.png);
    background-repeat: no-repeat;
    background-position: center;
}

.icon2 {
    display: block;
    float: left;
    margin-left: 30px;
    margin-top: 7px;
    height: 80%;
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
    margin-top: 20px;
}
</style>