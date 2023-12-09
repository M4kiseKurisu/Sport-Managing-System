<template>
    <div v-if="isSuccess">
        <el-result icon="申请活动成功" :title="msg" sub-title="Please follow the instructions">
            <template #extra>
                <el-button type="primary" @click="back">返回</el-button>
            </template>
        </el-result>
    </div>

    <div v-else>
        <el-result icon="申请活动失败" :title="msg" sub-title="Please follow the instructions">
            <template #extra>
                <el-button type="primary" @click="back">返回</el-button>
            </template>
        </el-result>
    </div>
</template>

<script>
export default {
    data() {
        return {

        }
    },
    methods: {
        back() {
            this.$router.push('/Page/MyActivity/Apply');
        }
    },
    props: ["isSuccess", "msg"]
}
</script>