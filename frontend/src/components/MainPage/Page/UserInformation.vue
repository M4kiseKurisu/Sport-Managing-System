<template>
    <el-row :gutter="20">
        <el-col :span="8">

            <!-- 头像组件 -->

            <div class="avatarDiv">
                <el-avatar :size="150" shape="circle" src="./src/images/emptyAvatar.png"></el-avatar>
            </div>

            <!-- 个人账号 -->

            <div class="nameDiv">
                <div>你好啊： </div>
                <div v-html="name"></div>
            </div>

            <!-- 个人签名 -->

            <div class="signDiv">
                <div v-html="sign"></div>
            </div>

            <el-divider />

            <!-- 个人数据 -->

            <div class="statistic">
                <el-row>
                    <el-col :span="8">
                        <el-statistic title="好友" :value="0" />
                    </el-col>
                    <el-col :span="8">
                        <el-statistic title="已参加活动" :value="0" />
                    </el-col>
                    <el-col :span="8">
                        <el-statistic title="已参加团体" :value="0" />
                    </el-col>
                </el-row>
            </div>
        </el-col>


        <el-col :span="8">

            <!-- 活动饼状图 -->
            <div class="pieChart">
                <Echart />
            </div>


        </el-col>


        <el-col :span="8">
        </el-col>
    </el-row>
</template>

<script>
import Echart from "../Components/Echart.vue"
export default {
    data() {
        return {
            name: 'MakiseKurisu',
            sign: '这个人很懒，还没有留下任何签名哦~'
        }
    },
    components: {
        Echart
    }
}
</script>

<style scoped>
.el-col {
    text-align: center;
}

.avatarDiv {
    display: flex;
    justify-content: center;
    padding-top: 20px;
}

.nameDiv {
    margin-top: 20px;
    display: flex;
    justify-content: center;
    font-size: 20px;
}

.signDiv {
    margin-top: 10px;
    display: flex;
    justify-content: center;
    font-size: 14px;
    color: gray;
}

.pieChart {
    display: flex;
    justify-content: center;
}
</style>
  