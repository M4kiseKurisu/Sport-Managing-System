<template>
    <div class="common-layout" v-if="stream">
        <el-container class="container">
            <!-- 姓名头像 -->
            <el-header class="header">
                <div v-if="stream.owner.picture !== null">
                    <img :src="'http://127.0.0.1:8000' + stream.owner.picture" class="avatar" />
                </div>
                <div v-else>
                    <img :src="defaultImage" class="avatar" />
                </div>
                <div class="name-timestamp">
                    <span class="name">{{ stream.owner.name }}</span>
                    <span class="timestamp">{{ stream.time }}</span>
                </div>

                <div class="delete-button" @click="deleteStream" v-if="stream.owner.name == myName">
                    删除动态
                </div>
            </el-header>

            <el-main>
                <!-- 图片文字 -->
                <div class="content">
                    <span class="activity" @click="checkInformation">
                        {{ "#" + this.stream.activity_name }}
                    </span>
                    <div class="spacer"></div>
                    <img :src="'http://127.0.0.1:8000' + stream.picture" class="streamPic" v-if="stream.picture !== null" />
                    <span class="streamText">{{ stream.text }}</span>
                </div>
            </el-main>
            <div class="spacer"></div>

            <el-footer class="footer">
                <div class="likeSection">
                    <!-- 点赞、展开 -->
                    <div>
                        <span v-if="liked" @click="toggleLike" class="likeButton">❤️</span>
                        <span v-else @click="toggleLike" class="likeButton">🤍</span>
                        <el-button v-if="stream.liker.length > 10" @click="toggleLikersDisplay" align="right">
                            <el-icon v-if="showLikers">
                                <Bottom />
                            </el-icon>
                            <el-icon v-else>
                                <Top />
                            </el-icon>
                        </el-button>
                    </div>
                    <!-- 点赞的人 -->
                    <div v-if="stream.liker && stream.liker.length > 0" class="likerList">
                        <div v-if="showLikers">
                            <span v-for="(liker, index) in stream.liker.slice(0, 7)" :key="index">
                                {{ liker.user_name }}
                                <span v-if="index < 6 && index < stream.liker.length - 1">, </span>
                            </span>
                        </div>
                        <div v-else>
                            <span v-for="(liker, index) in stream.liker" :key="index">
                                {{ liker.user_name }}
                                <span v-if="index < stream.liker.length - 1">, </span>
                            </span>
                        </div>

                    </div>
                </div>
            </el-footer>
            <el-divider />
        </el-container>
    </div>
</template>

<script>
import axios from 'axios';
import { Bottom, Top } from '@element-plus/icons-vue'
export default {
    data ()
    {
        return {
            stream: {
                "owner": {
                    "check": false,
                    "name": "杰少",
                    "picture": null
                },
                "sid": 43980362,
                "time": "2023-12-05 10:24:35",
                "text": "感谢大家支持！！！",
                "picture": null,
                "favor": 1,
                "is_favor": false,
                "liker": [
                ],
                "private": "所有人可见",
                "aid": 44709897,
                "activity_name": "RAOS 发布会"
            },
            defaultImage: "./src/images/group-default-picture.png",
            liked: this.stream.is_favor,
            showLikers: true,
            Bottom,
            Top,
            myName: JSON.parse( sessionStorage.getItem( "user_name" ) )
        }
    },
    props: {
        stream: {
            required: true
        }
    },
    components: {
        Bottom,
        Top
    },
    methods: {
        checkInformation ()
        {
            this.$router.push( '/Page/Activity_Information/Detail/' + this.stream.aid );
        },
        toggleLike ()
        {
            const uid = JSON.parse( sessionStorage.getItem( "uid" ) );
            axios.post( "http://127.0.0.1:8000/api/stream/favor", {
                uid: uid,
                sid: this.stream.sid
            } ).then( ( result ) =>
            {
                if ( result.data.status )
                {
                    this.liked = !this.liked
                }
                if ( this.liked )
                {
                    this.stream.liker.push( {
                        uid: uid,
                        user_name: JSON.parse( sessionStorage.getItem( "user_name" ) )
                    } )
                } else
                {
                    const index = this.stream.liker.findIndex(
                        ( liker ) => liker.uid === uid
                    );

                    // 如果找到索引，从数组中移除点赞者信息
                    if ( index !== -1 )
                    {
                        this.stream.liker.splice( index, 1 );
                    }
                }

            } );

        },
        toggleLikersDisplay ()
        {
            this.showLikers = !this.showLikers;
        },
        deleteStream ()
        {
            axios.post( "http://127.0.0.1:8000/api/stream/delete", {
                sid: this.stream.sid
            } ).then( ( result ) =>
            {
                if ( result.data.status )
                {
                    ElMessage.success( result.data.msg );
                    this.$emit( 'delete-stream', this.stream );
                    this.stream = [];
                } else
                {
                    ElMessage.error( result.data.msg );
                }
            } ).catch( error =>
            {
                console.error( 'Error deleting stream:', error );
                ElMessage.error( '删除失败，请重试' );
            } );
        }
    }
}

</script>


<style scoped>
.common-layout {
    padding: 0 20px;
    /* Margin on both sides of the container */
}

.container {
    margin: 0 auto;
    /* Center the container */
    max-width: 1200px;
    /* Maximum width of the container */
}

.header {
    display: flex;
    align-items: center;
}

.name-timestamp {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

/* 根据实际需要修改样式 */
.name {
    font-size: 20px;
    font-weight: bold;
    /* 其他样式 */
}

.timestamp {
    font-size: 14px;
    color: #999;
    /* 其他样式 */
}

.delete-button {
    cursor: pointer;
    margin-left: auto;
    /* 将按钮放置到最右边 */
    padding: 8px 16px;
    /* 按钮的内边距 */
    background-color: #d60404;
    /* 红色背景 */
    color: white;
    /* 文字颜色 */
    border: none;
    /* 去除边框 */
    border-radius: 4px;
    /* 圆角边框 */
}

.showform {
    margin-top: 20px;
}

.avatar {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    margin-right: 10px;
}

.activity {
    font-size: 20px;
    color: rgb(119, 12, 240);
    cursor: pointer;
}

.content {
    display: flex;
    flex-direction: column;
    margin-top: 20px;
    width: 90%;
    margin-left: 5%;
}

.streamPic {
    width: 30%;
}

.streamText {
    font-size: 20px;
}

.footer {
    width: 90%;
    margin-left: 5%;
}

.likeButton {
    cursor: pointer;
    align-self: left;
    /* 其他样式，如背景色、边框等 */
}

.likeSection {
    display: flex;
    flex-direction: column;
}

.likeButton {
    cursor: pointer;
    /* 其他样式，如背景色、边框等 */
}

.likerList {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
}

.likerList span {
    margin-right: 5px;
}

.spacer {
    height: 20px;
    /* 或者使用 margin 或 padding */
}
</style>