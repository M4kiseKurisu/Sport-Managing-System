<template>
    <div>
        <el-row :gutter="20">
            <div class="align">

                <!-- 活动名 -->
                <el-col :span="4">
                    <div class="text">{{ information.name }}</div>
                </el-col>

                <!-- 活动标签 -->
                <el-col :span="4">
                    <el-tag>{{ information.category }}</el-tag>
                </el-col>

                <!-- 开始时间 -->
                <el-col :span="5">
                    <div class="text">{{ information.start_time }}</div>
                </el-col>

                <!-- 结束时间 -->
                <el-col :span="5">
                    <div class="text">{{ information.end_time }}</div>
                </el-col>

                <!-- 查看详情 -->
                <el-col :span="4">
                    <el-button @click="check()">查看详情</el-button>
                </el-col>

            </div>
        </el-row>
    </div>
</template>

<script>
export default {
    data() {

    },
    methods: {
        check() {

        }
    },
    props: ["information"]
}
</script>

<style scoped>
.align {
    width: 80%;
    margin-left: 8%;
    display: flex;
    align-items: center;
}

.text {
    font-size: 16px;
}
</style>