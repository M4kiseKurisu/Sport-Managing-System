<template>
    <el-menu :default-active="activeIndex" mode="horizontal" router="true">
        <el-menu-item index="/Page/Activity_Information/Show">热门活动</el-menu-item>
        <el-menu-item index="/Page/Activity_Information/Before">过往活动</el-menu-item>
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