<template>
    <div class="card">
        <el-card :body-style="{}">
            <div class="title">
                <div class="size">
                    <img src="../../../images/basketball.png" class="pic" />
                </div>
                <div class="str1">{{ titleStr }}</div>
            </div>

            <div class="str2"> {{ contentStr }} </div>

            <div class="button">
                <el-button> 点击申请 </el-button>
            </div>
        </el-card>
    </div>
</template>

<script>
export default {
    data() {
        return {
        }
    },
    props: ["url", "titleStr", "contentStr"]
}
</script>

<style scoped>
.card {
    margin-left: 8%;
    margin-right: 8%;
}

.el-card {
    --el-card-border-radius: 10px;
    border-right: 4px solid #4c82ff63;
    border-bottom: 4px solid #4c82ff63;
}

.size {
    width: 80px;
    height: 80px;
}

.pic {
    background-repeat: no-repeat;
    background-position: center;
    object-fit: fill;
    width: 100%;
    height: 100%;
}

.title {
    display: flex;
    align-items: center;
    padding-left: 24px;
    padding-right: 16px;
}

.str1 {
    font-size: 22px;
    margin-left: 24px;
    font-weight: bold;
    margin-top: 12px;
}

.str2 {
    font-size: 16px;
    margin-left: 16px;
    margin-right: 16px;
    margin-top: 20px;
    font-style: italic;
}

.button {
    margin-top: 26px;
    display: flex;
    justify-content: center;
}
</style>