<template>
    <div class="location">
        <div v-if="isSuccess">
            <el-result icon="success" title="申请活动成功" :sub-title="msg">
                <!-- <template #extra>
                    <el-button type="primary" @click="back">返回</el-button>
                </template> -->
            </el-result>
        </div>

        <div v-else>
            <el-result icon="error" title="申请活动失败" :sub-title="msg">
                <!-- <template #extra>
                    <el-button type="primary" @click="back">返回</el-button>
                </template> -->
            </el-result>
        </div>
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

<style scoped>
.location {
    margin-left: -13%;
}
</style>