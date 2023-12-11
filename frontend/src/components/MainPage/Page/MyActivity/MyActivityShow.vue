<template>
    <div class="title">
        <div>我的活动</div>
    </div>

    <div>
        <el-row :gutter="20">
            <el-col :span="8">
                <Card />
            </el-col>

            <el-col :span="8">
                <Card />
            </el-col>

            <el-col :span="8">
                <Card />
            </el-col>
        </el-row>
    </div>
</template>

<script>
import Card from "../../Components/MyActivityShowCard.vue"
export default {
    data() {
        return {

        }
    },
    components: {
        Card,
    }
}
</script>

<style>
.title {
    font-size: 20px;
    margin-bottom: 16px;
    margin-top: 16px;
}
</style>