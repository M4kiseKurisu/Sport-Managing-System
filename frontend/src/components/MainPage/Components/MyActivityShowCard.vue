<template>
    <div class="border">
        <div class="header">
            <div class="topic">{{ name }}</div>


            <div class="like-button">
                <div class="heart-icon" :class="{ 'liked': liked }" @click="toggleLike">
                    <i class="fas fa-heart"></i>
                </div>
                <div class="like-count">{{ likeCount }}</div>
            </div>
        </div>

        <div class="text">开始时间：{{ start_time }}</div>
        <div class="text">结束时间：{{ end_time }}</div>
        <div class="text">活动类型：{{ category }}</div>
        <div class="text">活动人数/容量：{{ capacity }} / {{ maximum }}</div>
        <div class="buttonContainer">
            <div class="button">
                <el-button type="primary" @click="checkInformation()">查看详情</el-button>
                <el-button type="danger" @click="getOut()">退出/撤销活动</el-button>
                <el-button type="warning" v-if="judgeDate()" @click="this.show = true">发布活动动态</el-button>
            </div>
        </div>

    </div>

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
</template>

<script>
import axios from 'axios'
import dayjs from 'dayjs'
import { Delete, Download, Plus, ZoomIn } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus';
export default {
    data ()
    {
        return {
            liked: this.is_favor,
            likeCount: this.favor,
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
        }
    },
    components: {
        Delete,
        Download,
        Plus,
        ZoomIn,
    },
    methods: {
        toggleLike ()
        {
            if ( this.end_time > dayjs().format( 'YYYY-MM-DD HH:mm:ss' ) )
            {
                this.$message( {
                    showClose: true,
                    message: "不能在活动结束前点赞！",
                    type: 'error'
                } );
                return;
            }

            if ( this.liked )
            {
                let information = {
                    uid: JSON.parse( sessionStorage.getItem( 'uid' ) ),
                    aid: this.aid,
                    method: "remove"
                }

                axios( {
                    method: "POST",
                    url: "http://127.0.0.1:8000/api/activity/favor",
                    data: information
                } ).then( ( result ) =>
                {
                    if ( result.data.status )
                    {
                        this.$message( {
                            showClose: true,
                            message: result.data.msg,
                            type: 'success'
                        } );
                    }
                } );

                this.liked = !this.liked;
                this.likeCount--;
            }

            else
            {
                let information = {
                    uid: JSON.parse( sessionStorage.getItem( 'uid' ) ),
                    aid: this.aid,
                    method: "like"
                }

                axios( {
                    method: "POST",
                    url: "http://127.0.0.1:8000/api/activity/favor",
                    data: information
                } ).then( ( result ) =>
                {
                    if ( result.data.status )
                    {
                        this.$message( {
                            showClose: true,
                            message: result.data.msg,
                            type: 'success'
                        } );
                    }
                } );

                this.liked = !this.liked;
                this.likeCount++;
            }
        },
        checkInformation ()
        {
            this.$router.push( '/Page/Activity_Information/Detail/' + this.aid );
        },
        getOut ()
        {
            if ( this.start_time < dayjs().format( 'YYYY-MM-DD HH:mm:ss' ) )
            {
                this.$message( {
                    showClose: true,
                    message: "不能退出已经开始的活动！",
                    type: 'error'
                } );
                return;
            }

            let information = {
                uid: JSON.parse( sessionStorage.getItem( 'uid' ) ),
                aid: this.aid
            }

            axios( {
                method: "POST",
                url: "http://127.0.0.1:8000/api/activity/exit",
                data: information
            } ).then( ( result ) =>
            {
                if ( result.data.status )
                {
                    this.$message( {
                        showClose: true,
                        message: result.data.msg,
                        type: 'success'
                    } );
                }
            } );
        }, handlePicturePre ( file )
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
        },
        judgeDate ()
        {
            const currentTime = new Date();
            const endTime = new Date( this.end_time );
            return currentTime > endTime;
        }
    },
    props: [ "name", "start_time", "end_time", "category",
        "capacity", "maximum", "favor", "is_favor", "aid" ]
}
</script>

<style scoped>
.header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 15px;
}

.border {
    border: 4px solid #4c82ff63;
    border-radius: 8px;
    padding-top: 15px;
    padding-bottom: 15px;
    padding-left: 15px;
    padding-right: 15px;
}

.topic {
    font-size: 20px;
}

.text {
    font-size: 16px;
    margin-top: 10px;
}

.buttonContainer {
    margin-top: 20px;
    display: flex;
    justify-content: center;
}

.like-button {
    display: flex;
    align-items: center;
    height: 24px;
}

.heart-icon {
    cursor: pointer;
    width: 24px;
    height: 24px;
    margin-right: 8px;
    position: relative;
}

.heart-icon i {
    color: gray;
    transition: color 0.3s ease;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.liked i {
    color: red;
}

.like-count {
    font-weight: bold;
}
</style>