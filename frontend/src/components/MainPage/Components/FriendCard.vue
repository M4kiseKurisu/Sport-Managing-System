<template>
    <div class="user-card" v-if="showUserCard">
        <div class="avatar-container">
            <div v-if="user.pic !== null">
                <img class="avatar" :src="'http://127.0.0.1:8000' + user.pic" alt="User Avatar" />
            </div>
            <div>
                <img class="avatar" :src="'./src/images/group-default-picture.png'" alt="User Avatar" />
            </div>
        </div>
        <div class="user-info">
            <div class="user-name">{{ user.user_name }}</div>
            <div class="user-signature" v-if="user.signature !== ''">{{ user.signature }}</div>
            <div class="user-signature" v-else>这个人很懒，还没填写个人简介~</div>
        </div>
        <div class="button-row">
            <!-- <el-button type="text" @click="viewProfile" class="button">浏览好友主页</el-button> -->
            <el-button type="danger" @click="deleteUser(user)">删除好友</el-button>
        </div>

    </div>
</template>

<script>
import axios from 'axios'
export default {
    data ()
    {
        return {
            showUserCard: true,
        };
    },
    props: {
        user: {
            required: true
        }
    },
    methods: {
        deleteUser ( user )
        {
            ElMessageBox.confirm( '是否删除该好友',
                'Warning',
                {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning',
                }
            ).then( () =>
            {
                axios.post( 'http://127.0.0.1:8000/api/friend/delete', {
                    uid: sessionStorage.getItem( 'uid' ),
                    fid: user.uid,
                } ).then( response =>
                {
                    ElMessage( {
                        type: 'success',
                        message: '删除成功',
                    } );
                    this.showUserCard = false;
                } ).catch( error =>
                {
                    ElMessage( {
                        type: 'error',
                        message: '删除失败，请重试',
                    } );
                } );
            } ).catch( () =>
            {
                ElMessage( {
                    type: 'info',
                    message: '你已取消操作',
                } );
            } );
        },
        viewProfile ()
        {
            // Logic to view the user's profile
            // You can add your logic here to navigate to the user's profile page
        }
    }
};
</script>

<style scoped>
.user-card {
    display: flex;
    align-items: center;
    padding: 20px;
    border: 2px solid #ccc;
    border-radius: 10px;
    width: auth;
    height: 80px;
    /* 调整卡片宽度 */
    background: linear-gradient(to right, #ffafbd, #f8e3d7);
}

.avatar-container {
    justify-content: flex-start;
    /* 头像靠左对齐 */
    width: 100px;
    height: 100px;
    /* 调整头像容器高度 */
    border-radius: 50%;
    overflow: hidden;
    margin-bottom: 20px;
    margin-right: 20px;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
    background-color: white;
}

.avatar {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.user-info {
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    /* 垂直居中 */
}

.user-name {
    font-size: 20px;
    /* 调整字体大小 */
    font-weight: bold;
    margin-bottom: 8px;
}

.user-signature {
    color: #888;
    margin-bottom: 10px;
    font-size: 18px;
    /* 调整字体大小 */
}

.button-row {
    display: flex;
    justify-content: flex-end;
    /* 按钮靠右 */
    align-items: center;
    /* 垂直居中 */
}

.button-row .button {
    padding: 5px 10px;
    /* 调整按钮内边距 */
    background-color: #409eff;
    color: white;
    transition: background-color 0.3s;
}

.button-row .button:hover {
    background-color: #66b1ff;
    color: white;
    cursor: pointer;
}
</style>
