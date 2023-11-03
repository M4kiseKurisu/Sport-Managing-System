<template>
    <div id="background">
        <div class="firstrow">
            <div class="icon"></div>
            <div class="mainContent">
                <div class="shape1"></div>
                <div class="text1">去运动吧：</div>
                <div class="text2">MakiseKurisu</div>
            </div>
        </div>
        <hr color="lightgray" style="width:80%;text-align:left;margin-left:10%">
        <div class="secondrow">
            <div class="sign">这个人很懒，并没有留下个人签名哦~</div>
        </div>
        <div class="thirdrow">
            <div class="part">
                <div class="tip">好友</div>
                <div class="number">0</div>
            </div>
            <div class="line"></div>
            <div class="part">
                <div class="tip">团体</div>
                <div class="number">0</div>
            </div>
            <div class="line"></div>
            <div class="part">
                <div class="tip">活动</div>
                <div class="number">0</div>
            </div>
        </div>
        <hr color="lightgray" style="width:80%;text-align:left;margin-left:10%">
        <div class="fourthrow">
            <div class="tip2">请记得参加活动哦：</div>
            <div class="projectPic"></div>
            <div class="projectName">当前没有要参加的活动哦~</div>
        </div>
        <hr color="lightgray" style="width:80%;text-align:left;margin-left:10%">
        <div class="fifthrow">
            <div class="logo"></div>
            <div class="button">个人主页</div>
        </div>
    </div>
</template>

<script>
</script>

<style scoped>
#background {
    background-color: rgb(252, 252, 252);
    height: 600px;
    width: 360px;
    border-radius: 5px;
    padding-top: 30px;
}

.firstrow {
    width: 100%;
    height: 140px;
    display: flex;
}

.icon {
    height: 120px;
    width: 120px;
    border-radius: 60px;
    margin-left: 15px;
    margin-right: 15px;
    background-image: url(../images/animelogo2.png);
    background-repeat: no-repeat;
    background-position: center;
    background-size: 100% 100%;
    border: solid 1px grey;
    overflow: hidden;
}

.mainContent {
    width: 210px;
}

.shape1 {
    margin-top: -10px;
    margin-right: 10px;
    width: 130px;
    height: 30px;
    border-radius: 15px 15px 15px 15px;
    background: linear-gradient(220.55deg, #2AFADF 0%, #4C83FF 100%);
    float: right;
}

.text1 {
    margin-left: 10px;
    margin-top: 36px;
    font-size: 18px;
}

.text2 {
    margin-top: 8px;
    font-size: 24px;
    text-align: center;
    overflow: hidden;
}

.secondrow {
    width: 100%;
    margin-top: 5px;
    margin-bottom: 5px;
}

.thirdrow {
    margin-top: 10px;
    height: 80px;
    margin-bottom: 24px;
}

.sign {
    font-size: 14px;
    color: rgb(190, 190, 190);
    text-align: center;
}

.part {
    float: left;
    width: 119px;
    height: 100%;
}

.tip {
    margin-top: 8px;
    text-align: center;
    font-size: 14px;
}

.number {
    margin-top: 10px;
    text-align: center;
    font-size: 30px;
}

.line {
    width: 0.5px;
    height: 50px;
    background-color: lightgray;
    float: left;
    margin-top: 15px;
}

.fourthrow {
    width: 100%;
    margin-top: 24px;
    height: 220px;
}

.tip2 {
    font-size: 14px;
    text-align: left;
    margin-left: 36px;
    margin-bottom: 12px;
}

.projectPic {
    background-image: url(../images/animelogo.png);
    background-repeat: no-repeat;
    background-position: center;
    background-size: 100% 100%;
    margin-top: 8px;
    width: 90%;
    border: solid 1px black;
    height: 150px;
    margin-left: 18px;
}

.projectName {
    text-align: center;
    margin-top: 8px;
    font-size: 14px;
}

.fifthrow {
    margin-top: 8px;
    height: 60px;
}

.logo {
    float: left;
    width: 20px;
    height: 20px;
    background-image: url(../images/personalInformation2.png);
    background-repeat: no-repeat;
    background-position: center;
    background-size: 100% 100%;
    margin-top: 16px;
    margin-left: 36px;
}

.button {
    margin-top: 15px;
    font-size: 16px;
    margin-left: 36px;
    letter-spacing: 1px;
    float: left;
}
</style>