<template>
    <div>
        <el-row :gutter="20">
            <div class="align">

                <!-- 物品图像 -->
                <el-col :span="3">
                    <el-avatar v-if="!isTitle" :size="50" src="./src/images/basketball.png" />
                </el-col>

                <!-- 物品名 -->
                <el-col :span="3">
                    <div v-if="isTitle" class="text">器材类型</div>
                    <div v-else class="text">{{ information.name }}</div>
                </el-col>

                <!-- 物品数量 -->
                <el-col :span="2">
                    <div v-if="isTitle" class="text">借出数量</div>
                    <div v-else class="text">{{ information.amount }}</div>
                </el-col>

                <!-- 归还时间 -->
                <el-col :span="5">
                    <div v-if="isTitle" class="text">归还时间</div>
                    <div v-else class="text">{{ information.returnTime }}</div>
                </el-col>

                <!-- 借出团体 -->
                <el-col v-if="isGroup" :span="5">
                    <div v-if="isTitle" class="text">借出团体</div>
                    <div v-else class="text">{{ information.group }}</div>
                </el-col>

                <!-- 归还状态 -->
                <el-col :span="3">
                    <div v-if="isTitle" class="text">归还状态</div>
                    <div v-else class="text">{{ information.state }}</div>
                </el-col>

                <!-- 归还按钮 -->
                <el-col :span="3">
                    <div v-if="isTitle" class="text">归还操作</div>
                    <el-button v-else-if="information.state === '未归还'" type="primary">归还器材</el-button>
                    <el-button v-else disabled type="primary">归还器材</el-button>
                </el-col>
            </div>
        </el-row>
        <div v-if="isTitle" style="margin-bottom: 6px;"></div>
        <hr v-if="isGroup" class="divider1">
        <hr v-else class="divider2">
    </div>
</template>

<script>
export default {
    data() {
        return {

        }
    },
    props: ["information", "isTitle", "isGroup"]
}
</script>

<style scoped>
.divider1 {
    width: 84%;
    margin-left: 6%;
    margin-top: 2px;
    margin-bottom: 2px;
    color: gray;
}

.divider2 {
    width: 68%;
    margin-left: 6%;
    margin-top: 2px;
    margin-bottom: 2px;
    color: gray;
}

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