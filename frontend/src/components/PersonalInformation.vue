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
            妹妹呢，我要妹妹，妹妹，妹妹，妹妹，妹妹！！！！！！！
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
    height: 80px;
    color: red;
    font-size: 30px;
}
</style>