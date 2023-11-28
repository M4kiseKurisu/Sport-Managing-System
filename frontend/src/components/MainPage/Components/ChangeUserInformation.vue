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
import { Plus } from '@element-plus/icons-vue'
import axios from "axios";
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
                signature: '',
            },
        }
    },
    methods: {
        clickApply() {
            this.dialogVisible = true;
            axios({
                method: "GET",
                url: "http://127.0.0.1:8000/api/user/information",
                params: {
                    uid: JSON.parse(sessionStorage.getItem("uid")),
                },
            }).then((result) => {
                if (result.data.status) {
                    this.form.name = result.data.info.name;
                    this.form.age = result.data.info.age;
                    this.form.gender = result.data.info.gender;
                    this.form.phone = result.data.info.phone;
                    this.form.email = result.data.info.email;
                    this.form.signature = result.data.info.signature;
                }
            });
        },
        onSubmit() {
            let content = {
                user_name: this.form.name,
                user_age: this.form.age,
                user_gender: this.form.gender === '女' ? 0 : 1,
                phone_number: this.form.phone,
                email: this.form.email,
                user_signature: this.form.signature,
            };

            let apply = {
                uid: JSON.parse(sessionStorage.getItem('uid')),
                data: content
            }

            axios({
                method: "POST",
                url: "http://127.0.0.1:8000/api/user/modify/text",
                uid: JSON.parse(sessionStorage.getItem('uid')),
                data: apply
            }).then((result) => {
                //console.log(result);
                if (result.data.status) {
                    this.$message({
                        showClose: true,
                        message: result.data.msg,
                        type: 'success'
                    });
                } else {
                    this.$message({
                        showClose: true,
                        message: result.data.msg,
                        type: 'error'
                    });
                }
            })
        }
    },
    components: {
        Plus,
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

.right {
    display: flex;
}

.buttons {
    margin-left: 30px;
}

.preview-container {
    display: flex;
    flex-wrap: wrap;
    margin-top: 10px;
}

.preview-image {
    width: 200px;
    height: 200px;
    object-fit: cover;
    margin-right: 10px;
    margin-bottom: 10px;
}
</style>