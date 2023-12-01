<template>
    <div class="all">
        <!-- 用户头像 -->
        <el-avatar :src="'http://127.0.0.1:8000' + participant.picture" />


        <!-- 用户姓名 -->
        <div class="text">
            {{ participant.user_name }}
        </div>

        <!-- 用户性别 -->
        <el-icon v-if="this.gender === '女'">
            <Female />
        </el-icon>
        <el-icon v-else>
            <Male />
        </el-icon>


    </div>
</template>

<script>
import { Female, Male } from "@element-plus/icons-vue";
export default {
    data() {

    },
    components: {
        Female,
        Male,
    },
    props: ["participant"]
}
</script>

<style scoped>
.all {
    display: flex;
    align-items: center;
    margin-top: 6px;
    margin-bottom: 6px;
}

.text {
    font-size: 16px;
    margin-left: 16px;
    margin-right: 12px;
}
</style>