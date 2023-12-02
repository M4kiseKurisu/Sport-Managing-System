<template>
    <!-- 搜索框 -->
    <div class="searchTitleNew">
        <div class="searchBoxNew">
            <el-input v-model="searchKeyword" placeholder="输入好友昵称"></el-input>
        </div>
        <el-button @click="searchFriends" class="searchButtonNew">查询</el-button>
    </div>

    <!-- 搜索结果 -->
    <div class="friend-list">
        <el-table :data="filteredSearchFriends" style="width: 100%">
            <!-- 列表展示 -->
            <el-table-column label="呢称">
                <template #default="scope">
                    <div v-for="friend in scope.row" :key="friend.uid" class="friend-info">
                        <div v-if="friend.pic !== null">
                            <img :src="'http://127.0.0.1:8000' + friend.pic" class="avatar" />
                        </div>
                        <div v-else>
                            <img :src="defaultImage" class="avatar" />
                        </div>
                        <span>{{ friend.user_name }}</span>
                    </div>
                </template>
            </el-table-column>


            <el-table-column label="个性签名">
                <!-- 根据搜索结果渲染列表 -->
                <template #default="scope">
                    <div v-for="friend in scope.row" :key="friend.uid">
                        {{ friend.signature }}
                    </div>
                </template>
            </el-table-column>


            <el-table-column align="center" label="申请添加">
                <!-- 根据搜索结果渲染不同的按钮 -->
                <template #default="scope">
                    <div v-for="friend in scope.row" :key="friend.uid">
                        <el-button v-if="!isFriend(friend)" size="small" type="primary" @click="addFriend(friend)">
                            添加好友
                        </el-button>
                        <el-button v-else size="small" type="primary" disabled>
                            已添加
                        </el-button>
                    </div>
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>

<script lang="js">
import axios from 'axios';

export default {
    data ()
    {
        return {
            newFriends: [],
            defaultImage: "./src/images/group-default-picture.png",
            searchKeyword: '',
            // Other data properties...
        };
    },

    computed: {
        filteredSearchFriends ()
        {
            let filterfriends = [];
            for ( let i = 0; i < this.newFriends.length; i += 10 )
            {
                filterfriends.push( this.newFriends.slice( i, i + 10 ) );
            }

            return filterfriends;
        }
    },

    methods: {
        searchFriends ()
        {
            // 发起搜索请求
            axios.get( 'http://127.0.0.1:8000/api/user/find', {
                params: {
                    uid: sessionStorage.getItem( 'uid' ),
                    keyword: this.searchKeyword,
                },
            } )
                .then( ( result ) =>
                {
                    if ( result.data.status )
                    {
                        this.newFriends = result.data.list;
                        this.msg = result.data.msg;
                    }
                } )
                .catch( ( error ) =>
                {
                    console.error( 'Error fetching friend data:', error );
                } );
        },

        addFriend ( friend )
        {
            ElMessageBox.prompt( '发送你的申请', {
                confirmButtonText: '提交申请',
                cancelButtonText: '取消申请',
                inputPattern: /.*/,
                inputErrorMessage: '请填写申请',
            } ).then( ( { value } ) =>
            {
                if ( !value )
                {
                    ElMessage( {
                        type: 'warning',
                        message: '申请信息不能为空',
                    } );
                    return;
                }

                // 发送申请
                axios.post( 'http://127.0.0.1:8000/api/friend/add', {
                    sender: sessionStorage.getItem( 'uid' ),
                    receiver: friend.uid,
                    content: value,
                } ).then( response =>
                {
                    const { status, msg } = response.data;
                    if ( status === true )
                    {
                        ElMessage( {
                            type: 'success',
                            message: msg,
                        } );
                    } else
                    {
                        ElMessage( {
                            type: 'error',
                            message: msg,
                        } );
                    }
                } ).catch( error =>
                {
                    console.error( '发送申请时出错:', error );
                    ElMessage( {
                        type: 'error',
                        message: '申请发送失败，请稍后重试',
                    } );
                } );
            } ).catch( () =>
            {
                ElMessage( {
                    type: 'info',
                    message: '你已取消申请',
                } );
            } );
        },

        getAvatar ( friend )
        {
            return friend.pic;
        },
        isFriend ( friend )
        {
            // 这里根据 friend 是否是好友进行判断
            return friend.is_friend === true;
        },
    }
};
</script>

<style scoped>
.searchTitleNew {
    width: 100%;
    display: flex;
    justify-content: flex-end;
    /* 将元素靠右对齐 */
    padding: 10px 0;
    /* 添加上下边距 */
}

.searchBoxNew {
    width: 250px;
    margin-left: auto;
    /* 使用 auto 来推动搜索框到最右边 */
    margin-right: 10px;
    /* 添加一些右边距以便与按钮分隔 */
}

.searchButtonNew {
    width: 80px;
}

/* 表格样式 */
.friend-list {
    max-height: 400px;
    /* 调整列表最大高度 */
    overflow-y: auto;
    /* 当内容超出高度时显示滚动条 */
}

.friend-info {
    display: flex;
    align-items: center;
}

.avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 10px;
}
</style>