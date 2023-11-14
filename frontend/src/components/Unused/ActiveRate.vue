<template>
    <div class="background">
        <div class="title">您过去60天的参加活动情况：</div>
        <div class="content">
            <div class="row">
                <div class="gray"></div>
                <div class="gray"></div>
                <div class="gray"></div>
                <div class="light"></div>
                <div class="gray"></div>
                <div class="gray"></div>
                <div class="gray"></div>
                <div class="dark"></div>
                <div class="gray"></div>
                <div class="gray"></div>
                <div class="dark"></div>
                <div class="gray"></div>
                <div class="gray"></div>
                <div class="gray"></div>
                <div class="gray"></div>
                <div class="light"></div>
                <div class="gray"></div>
                <div class="gray"></div>
                <div class="light"></div>
                <div class="gray"></div>
            </div>
            <div class="row">
                <div class="gray"></div>
                <div class="gray"></div>
                <div class="gray"></div>
                <div class="light"></div>
                <div class="gray"></div>
                <div class="gray"></div>
                <div class="light"></div>
                <div class="dark"></div>
                <div class="gray"></div>
                <div class="gray"></div>
                <div class="dark"></div>
                <div class="dark"></div>
                <div class="gray"></div>
                <div class="gray"></div>
                <div class="gray"></div>
                <div class="light"></div>
                <div class="gray"></div>
                <div class="gray"></div>
                <div class="light"></div>
                <div class="dark"></div>
            </div>
            <div class="row">
                <div class="gray"></div>
                <div class="gray"></div>
                <div class="gray"></div>
                <div class="light"></div>
                <div class="gray"></div>
                <div class="gray"></div>
                <div class="gray"></div>
                <div class="light"></div>
                <div class="light"></div>
                <div class="gray"></div>
                <div class="dark"></div>
                <div class="gray"></div>
                <div class="gray"></div>
                <div class="light"></div>
                <div class="gray"></div>
                <div class="light"></div>
                <div class="gray"></div>
                <div class="gray"></div>
                <div class="light"></div>
                <div class="gray"></div>
            </div>
        </div>
        <div class="line"></div>
        <div class="explain">
            <div class="row2">
                <div class="gray"></div>
                <div class="tip">灰色代表当天未参加活动</div>
            </div>
            <div class="row2">
                <div class="light"></div>
                <div class="tip">浅蓝色代表当天参加一次活动</div>
            </div>
            <div class="row2">
                <div class="dark"></div>
                <div class="tip">深蓝色代表当天参加多次活动</div>
            </div>
        </div>
    </div>
</template>

<script>
</script>

<style scoped>
.background {
    background-color: rgb(252, 252, 252);
    height: 140px;
    width: 740px;
    border-radius: 5px;
    padding-top: 20px;
}

.title {
    margin-left: 40px;
}

.content {
    margin-left: 24px;
    margin-top: 20px;
    margin-bottom: 20px;
    height: 60px;
    width: 360px;
    float: left;
}

.line {
    float: left;
    height: 55px;
    width: 0.6px;
    margin-top: 40px;
    margin-left: 80px;
    background-color: lightgray;
}

.explain {
    margin-top: 40px;
    margin-right: 12px;
    float: right;
    width: 240px;
    height: 65px;
}

.row {
    height: 20px;
    width: 100%;
}

.gray {
    width: 14px;
    height: 14px;
    border-radius: 7px 7px 7px 7px;
    background-color: lightgrey;
    margin: 2px 2px 2px 2px;
    float: left;
}

.light {
    width: 14px;
    height: 14px;
    border-radius: 7px 7px 7px 7px;
    background-color: #2AFADF;
    margin: 2px 2px 2px 2px;
    float: left;
}

.dark {
    width: 14px;
    height: 14px;
    border-radius: 7px 7px 7px 7px;
    background-color: #4C83FF;
    margin: 2px 2px 2px 2px;
    float: left;
}

.tip {
    font-size: 14px;
    color: gray;
    margin-left: 28px;
}
</style>
