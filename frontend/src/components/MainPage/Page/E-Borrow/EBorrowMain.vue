<template>
    <el-menu mode="horizontal" router="true">
        <el-menu-item index="/Borrow_Equipment/Equipment_Information">器材租借</el-menu-item>
        <el-menu-item index="/Borrow_Equipment/Personal_Borrow">我的借还情况</el-menu-item>
    </el-menu>
    <router-view></router-view>
</template>

<script>
export default {
    data() {
        return {

        }
    }
}
</script>