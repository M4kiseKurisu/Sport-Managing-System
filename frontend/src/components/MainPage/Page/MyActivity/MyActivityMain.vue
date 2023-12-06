<template>
    <el-menu :default-active="activeIndex" mode="horizontal" router="true">
        <el-menu-item index="/Page/MyActivity/Show">我的活动</el-menu-item>
        <el-menu-item index="/Page/MyActivity/Apply">申请活动</el-menu-item>
    </el-menu>
    <router-view></router-view>
</template>

<script>
export default {
    data() {
        return {
            activeIndex: "/Activity_Information/Show"
        }
    }
}
</script>

<style scoped>
.el-menu-item {
    font-size: 16px;
}

.fontsize {
    font-size: 16px;
}
</style>