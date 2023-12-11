<template>
    <div>
        <el-button text @click="this.show = true">发布动态</el-button>
        <el-dialog v-model="show">
            <el-form :model="form" label-width="120px" :rules="rules">
                <el-form-item label="动态文本" prop="text">
                    <el-input v-model="form.text" style="width: 150px;" show-word-limit />
                </el-form-item>
                <el-form-item label="设置权限" prop="permission">
                    <el-select v-model="form.private" placeholder="please select your zone">
                        <el-option label="仅自己可见" value="0" />
                        <el-option label="仅好友可见" value="1" />
                        <el-option label="所有人可见" value="2" />
                    </el-select>
                </el-form-item>

                <!-- 上传逻辑 -->
                <el-form-item label="上传图片" prop="pic">
                    <el-upload action="#" list-type="picture-card" :auto-upload="false" :limit="1" :on-remove="handleRemove"
                        v-model:file-list="this.form.pic">
                        <el-icon>
                            <Plus />
                        </el-icon>

                        <template #file="{ file }">
                            <div>
                                <img class="el-upload-list__item-thumbnail" :src="file.url" alt="" />
                                <span class="el-upload-list__item-actions">
                                    <span class="el-upload-list__item-preview" @click="handlePicturePre(file)">
                                        <el-icon><zoom-in /></el-icon>
                                    </span>
                                    <span class="el-upload-list__item-preview" @click="handleRemove(file, this.form.pic)">
                                        <el-icon>
                                            <Delete />
                                        </el-icon>
                                    </span>
                                </span>
                            </div>
                        </template>

                        <template #tip>
                            <div class="el-upload__tip" style="color: red;">
                                最多上传一张图片
                            </div>
                        </template>
                    </el-upload>

                    <el-dialog v-model="dialogVisible">
                        <img w-full :src="dialogImageUrl" alt="Preview Image" />
                    </el-dialog>

                    <!-- 上传逻辑 -->
                </el-form-item>
            </el-form>
            <template #footer>
                <span class="dialog-footer">
                    <el-button @click="showCreateMoment
                        = false">取消</el-button>
                    <el-button type="primary" @click="onSubmit">
                        提交
                    </el-button>
                </span>
            </template>
        </el-dialog>
    </div>
</template>

<script>
import axios from 'axios'
import { Delete, Download, Plus, ZoomIn } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus';
export default {
    data ()
    {
        return {
            show: false,
            dialogVisible: false,
            form: {},
            dialogImageUrl: '',
            rules: {
                text: [
                    { required: true, message: '请填写动态文本', trigger: 'blur' },
                ],
                permission: [
                    { required: true, message: '请设置权限', trigger: 'blur' },
                ],
                pic: [
                    { required: true, message: '请上传图片', trigger: 'blur' },
                ],
            },
            aid: 53357698,
        }
    },
    components: {
        Delete,
        Download,
        Plus,
        ZoomIn,
    },
    methods: {
        handlePicturePre ( file )
        {
            this.dialogImageUrl = file.url;
            this.dialogVisible = true;
        },

        handleRemove ( uploadFile, uploadFiles )
        {
            const index = uploadFiles.indexOf( uploadFile );
            if ( index !== -1 )
            {
                uploadFiles.splice( index, 1 );
                uploadFile.url = '';
            }
            this.dialogImageUrl = '';
        },
        onSubmit ()
        {
            console.log( this.form.text )
            console.log( this.form.private )
            console.log( this.form.pic.length )
            if ( this.form.text && this.form.private
                && this.form.pic.length != 0 )
            {
                const pic = this.form.pic[ 0 ].raw
                const data = new FormData();
                const uid = sessionStorage.getItem( 'uid' );
                if ( uid )
                {
                    data.append( 'uid', uid );
                }
                data.append( 'aid', this.aid );
                data.append( 'text', this.form.text );
                data.append( 'private', this.form.private );
                data.append( 'picture', pic );

                axios.post( 'http://127.0.0.1:8000/api/stream/publish', data )
                    .then( response =>
                    {
                        if ( response.data.status )
                        {
                            this.$message.success( '发布成功' );
                        } else
                        {
                            this.$message.error( '发布失败，请重试' );
                        }
                    } )
                this.show = false
            } else
            {
                ElMessage.error( '请填写必填项！' );
            }
        }
    }
}

</script>