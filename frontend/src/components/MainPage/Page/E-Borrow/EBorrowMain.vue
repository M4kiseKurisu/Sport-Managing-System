<template>
    <el-menu :default-active="activeIndex" mode="horizontal" router="true">
        <el-menu-item index="/Borrow_Equipment/Equipment_Information">器材租借</el-menu-item>
        <el-sub-menu>
            <template #title>
                <div class="fontsize">
                    我的借还情况
                </div>
            </template>
            <el-menu-item index="/Borrow_Equipment/Borrow/Personal">个人借出</el-menu-item>
            <el-menu-item index="/Borrow_Equipment/Borrow/Group">团体借出</el-menu-item>
        </el-sub-menu>
    </el-menu>
    <router-view></router-view>
</template>

<script>
export default {
    data() {
        return {
            activeIndex: ""
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