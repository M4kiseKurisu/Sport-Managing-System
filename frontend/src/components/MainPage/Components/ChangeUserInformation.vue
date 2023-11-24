<template>
    <el-button @click="clickApply()" type="primary" plain> 更改个人信息 </el-button>
    <el-dialog v-model="dialogVisible" title="更新个人信息" width="50%">

        <div class="form">
            <el-form :model="form" label-width="120px">
                <el-form-item label="用户昵称">
                    <el-input v-model="form.name" />
                </el-form-item>

                <div class="row">
                    <el-form-item label="年龄">
                        <el-input-number v-model="form.age" :min="1" :max="100" />
                    </el-form-item>

                    <el-form-item label="性别">
                        <el-radio-group v-model="form.gender">
                            <el-radio label="男" />
                            <el-radio label="女" />
                        </el-radio-group>
                    </el-form-item>
                </div>

                <div class="row">
                    <el-form-item label="电话号码">
                        <el-input v-model="form.phone" />
                    </el-form-item>

                    <el-form-item label="电子邮箱">
                        <el-input v-model="form.email" />
                    </el-form-item>
                </div>

                <el-form-item label="个人签名">
                    <el-input v-model="form.signature" type="textarea" />
                </el-form-item>

                <div class="commitButton">
                    <el-form-item>
                        <el-button type="primary" @click="onSubmit">确认更改</el-button>
                    </el-form-item>
                </div>


            </el-form>
        </div>

    </el-dialog>
</template>

<script>
export default {
    data() {
        return {
            dialogVisible: false,
            form: {
                name: '',
                age: '',
                gender: '',
                phone: '',
                email: '',
                signature: ''
            },
        }
    },
    methods: {
        clickApply() {
            this.dialogVisible = true;
        },
        onSubmit() {
            //提交新的身份信息
        }
    }
}
</script>

<style scoped>
.form {
    padding-right: 10%;
}

.el-form {
    --el-form-label-font-size: 16px;
}

.row {
    display: flex;
}

.commitButton {
    margin-top: 20px;
}
</style>