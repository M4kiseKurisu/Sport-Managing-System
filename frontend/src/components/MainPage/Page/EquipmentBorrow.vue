<template>
    <!-- 界面标题 -->
    <div class="title">
        <div>器材借还</div>
    </div>

    <el-divider />

    <el-row :gutter="20">

        <el-col :span="14">
            <!-- 左侧小标题 -->
            <div class="subtitle">当前器材情况</div>

            <!-- 学校器材情况表 -->
            <div class="form">
                <Form />
            </div>
        </el-col>


        <el-col :span="10">
            <!-- 右侧小标题 -->
            <div class="subtitle">我的借还</div>
        </el-col>

    </el-row>
</template>

<script>
import Form from "../Components/Form.vue"
export default {
    data() {
        return {

        }
    },
    components: {
        Form,
    }
}
</script>

<style scoped>
.title {
    font-size: 20px;
    margin-bottom: 16px;
    margin-top: 16px;
}

.subtitle {
    margin-top: 10px;
    font-size: 18px;
}

.form {
    margin-top: 20px;
    display: flex;
    justify-content: center;
}
</style>