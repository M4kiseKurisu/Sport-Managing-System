<template>
    <el-scrollbar height="400px">
        <el-card class="activity-card" v-for="(activity, index) in activityList" :key="index"
            @click="viewActivity(activity.aid)">
            <div class="card-content">
                <div class="image-container">
                    <div class="image-blurred"
                        :style="{ backgroundImage: 'url(' + 'http://127.0.0.1:8000' + activity.picture + ')' }"></div>
                </div>
                <div class="info">
                    <h3 class="activity-name">{{ activity.name }}</h3>
                    <p class="activity-time">{{ activity.start_time }} ~ {{ activity.end_time }}</p>
                    <p class="activity-category">{{ activity.category }}</p>
                    <p class="activity-favor">❤️{{ activity.favor }}</p>
                    <p class="activity-capacity">{{ activity.capacity }} / {{ activity.maximum }}</p>
                </div>
            </div>
        </el-card>
    </el-scrollbar>
</template>

<script>
import axios from 'axios'
export default {
    data ()
    {
        return {
            activityList: [],
        };
    },
    created ()
    {
        this.getData();
    },
    props: {
        gid: String,
    },
    methods: {
        getData ()
        {
            console.log( this.gid )
            if ( this.gid !== "" )
            {
                // console.log( "data: " + this.gid )
                axios( {
                    method: "GET",
                    url: "http://127.0.0.1:8000/api/group/activity/view",
                    params: {
                        gid: this.gid
                    }
                } ).then( ( result ) =>
                {
                    if ( result.data.status )
                    {
                        this.activityList = result.data.list; // 将后端数据赋值给 Users
                    }
                } ).catch( ( error ) =>
                {
                    console.error( "Error fetching group data:", error );
                } );
            }
        },
        viewActivity ( aid )
        {
            this.$router.push( '/Page/Activity_Information/Detail/' + aid );
        }
    },
};
</script>

<style>
.activity-card {
    width: 99%;
    /* 根据需要设置其他样式 */
}

.card-content {
    display: flex;
    position: relative;
}


.image-blurred {
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    filter: blur(5px);
    /* 添加虚化效果 */
    position: absolute;
    top: 0;
    left: 0;
    /* 确保图片在内容之后 */
}

.info {
    width: 100px;
    height: 80px;
    flex: 1;
    position: relative;

    background-color: rgba(185, 185, 185, 0.021);
    padding: 5px;
    border-radius: 5px;
    margin-bottom: 5px;
    /* 将内容区域设为相对定位 */
}

.activity-name {
    text-align: center;
    color: white;
    text-shadow: 1px 1px 2px black;
    /* 调整阴影效果 */
}

.activity-time {
    margin-bottom: 5px;
    text-align: center;
    color: white;
    text-shadow: 1px 1px 2px black;
    /* 调整阴影效果 */
}

.activity-favor {
    position: absolute;
    bottom: 5px;

}

.activity-capacity {
    position: absolute;
    bottom: 5px;
    right: 5px;
    color: white;
    text-shadow: 1px 1px 2px black;
    /* 调整阴影效果 */
}

.activity-category {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 5px;
    background-color: rgb(135, 198, 235);

    position: absolute;
    top: 0px;
    font-weight: bold;

    /* 其他样式 */
}

/* 根据需要设置其他样式 */
</style>
