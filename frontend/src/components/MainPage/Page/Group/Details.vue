<template>
  <div class="common-layout">
    <el-container>

      <el-aside width="200px" class="centered-aside">
        <div class="group-info">
          <div class="group-details">
            <div class="center-content">
              <div v-if="group.image !== null">
                <img :src="'http://127.0.0.1:8000' + group.image" class="image enlarged-image" />
              </div>
              <div v-else>
                <img :src="defaultImage" class="image enlarged-image" />
              </div>
              <div class="group_name">
                <h1 class="enlarged-name">{{ group.name }}</h1>
              </div>
              <!-- <div class="group-buttons" v-if="this.father == 'YourGroup'
                && (this.group.type == '创建人' || this.group.type == '管理员')">
                <el-button @click="addActivity()">新增活动</el-button>
              </div> -->
            </div>
          </div>
        </div>
      </el-aside>


      <el-main width="800px">

        <div class="group-navigation">
          <!-- Right section for navigation -->

          <el-card>
            <ul @click="openActivity = true">
              <li>团体活动</li>
            </ul>
            <el-divider />
            <div class="activity-layout">
              <el-container>
                <el-aside width="300px">
                  <div ref="chart" style="width: 300px; height: 300px;" class="group-activity"></div>
                </el-aside>
                <el-divider direction="vertical" style="height: 400px;"></el-divider>
                <el-main>
                  <GroupActivityCard :gid="this.$route.query.gid" class="GroupActivityCard" />
                </el-main>
              </el-container>
            </div>
          </el-card>

          <el-card>
            <el-collapse v-model="activeName" accordion>
              <el-collapse-item name="1" class="group_instrudiction">
                <template #title class="collapse_title">
                  <span class="custom-collapse-title">团体简介</span>
                </template>
                <p>{{ group.description }}</p>
              </el-collapse-item>
            </el-collapse>
          </el-card>
          <ul>
            <el-card @click="drawer = true">
              <li>其他成员</li>
            </el-card>
            <!-- Add more navigation links as needed -->
          </ul>
        </div>
      </el-main>
    </el-container>

    <el-drawer v-model="drawer" :open-method="getData()" title="成员列表" :with-header="false" size="630px">
      <div class="custom-table">
        <div class="table-row header">
          <div class="table-cell">呢称</div>
          <div class="table-cell">类型</div>
          <div class="table-cell">操作</div>
        </div>

        <div v-for="user in filteredUsers[currentPage - 1]" :key="user.uid" class="table-row">
          <div class="table-cell">
            <div class="user-info">
              <div v-if="user.pic !== null">
                <img :src="'http://127.0.0.1:8000' + user.pic" class="avatar" />
              </div>
              <div class="user-name">
                <span>{{ user.user_name }}</span>
              </div>
            </div>
          </div>

          <div class="table-cell">
            <div class="type">
              <span>{{ user.type }}</span>
            </div>
          </div>

          <div class="table-cell">
            <div v-if="father == 'YourGroup'" class="button-container">
              <el-button v-if="this.group.type == '创建人' || (this.group.type == '管理员'
                && user.type == '成员')" size="small" type="danger" @click="handleDelete(user.uid)">踢出</el-button>
              <el-button v-if="this.group.type == '创建人'" size="small" type="warning" @click="handleSet(user)">
                <span v-if="user.type == '管理员'">移除权限</span>
                <span v-if="user.type == '成员'">设为管理员</span>
              </el-button>
            </div>
          </div>
        </div>
      </div>

      <el-pagination :small="small" :disabled="disabled" :background="background" layout="prev, pager, next"
        :page-size="10" :total="totalPages" v-model:current-page="currentPage" @current-change="handleCurrentChange" />
    </el-drawer>

  </div>
</template>

<script lang="js">
import axios from 'axios'
import * as echarts from 'echarts';
import GroupActivityCard from '../../Components/GroupActivityCard.vue';

export default {
  data ()
  {
    return {
      select: "",
      drawer: false,
      group: {
        gid: "",
        image: "./src/images/group-default-picture.png",
        name: "团体名称",
        description: "团体简介描述",
        type: ""
      },
      father: "",
      Users: [],
      small: false,
      background: false,
      disabled: false,
      keyword: "",
      currentPage: 1,
      defaultImage: "./src/images/group-default-picture.png",
      activeName: "",
      showActivity: "",
      gid: "",
      option: {
        title: {
          text: '团队活动统计',
          left: 'center'
        },
        tooltip: {
          trigger: "item",
        },
        legend: {
          orient: 'vertical',
          top: "5%",
          left: "left"
        },
        series: [
          {
            name: "该类型数量",
            type: "pie",
            radius: [ "40%", "70%" ],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: "#fff",
              borderWidth: 2
            },
            label: {
              rotate: 0, // 文本旋转角度，单位为度（逆时针方向为正）
              show: true, // 是否显示标签
              overflow: 'truncate', // 文本溢出截断，可以是 'truncate' 或者 'break'
              position: 'outer', // 标签位置，'outer' 表示外部，可以是 'inner' 内部
              alignTo: 'none', // 对齐方式，例如 'labelLine' 或 'none'
              edgeDistance: '25%', // 边缘距离，例如 '10%' 或者具体数值
              bleedMargin: 10, // 超出边缘的补偿大小
              distanceToLabelLine: 5 // 标签与标签引导线之间的距离
            },
            emphasis: {
              label: {
                show: true,
                fontSize: 25,
                fontWeight: "bold"
              }
            },
            labelLine: {
              show: true
            },
            data: [
              { value: 1048, name: "Search Engine" },
              { value: 735, name: "Direct" },
              { value: 580, name: "Email" },
              { value: 484, name: "Union Ads" },
              { value: 300, name: "Video Ads" }
            ]
          }
        ]
      },
      myOpData: []
    };
  },
  mounted ()
  {
    // 获取传递的参数
    const gid = this.$route.query.gid;
    const groupName = this.$route.query.groupName;
    const description = this.$route.query.description;
    const image = this.$route.query.image;
    const father = this.$route.query.father;
    const type = this.$route.query.type;
    // 将参数存储在 group 对象中
    this.group.gid = gid;
    this.gid = gid;
    this.group.name = groupName;
    this.group.description = description;
    this.group.image = image;
    this.group.type = type;
    this.father = father;
    this.getData();
    this.getMyOpData();
  },
  computed: {
    totalPages ()
    {
      return Math.ceil( this.Users.length );
    },
    filteredUsers ()
    {
      let buf = [];
      let filterUsers = [];
      for ( let i = 0; i < this.Users.length; i++ )
      {
        if ( this.Users[ i ].uid != sessionStorage.getItem( "uid" ) )
        {
          buf.push( this.Users[ i ] );
        }
      }
      for ( let i = 0; i < buf.length; i += 10 )
      {
        filterUsers.push( buf.slice( i, i + 10 ) );
      }
      console.log( filterUsers )
      return filterUsers;
    },
  },
  methods: {
    getData ()
    {
      if ( this.gid !== "" )
      {
        // console.log( "data: " + this.gid )
        axios( {
          method: "GET",
          url: "http://127.0.0.1:8000/api/group/members/list",
          params: {
            gid: this.gid
          }
        } ).then( ( result ) =>
        {
          if ( result.data.status )
          {
            this.Users = result.data.list; // 将后端数据赋值给 Users
            this.msg = result.data.msg;
          }
        } ).catch( ( error ) =>
        {
          console.error( "Error fetching group data:", error );
        } );
      }
    },
    search ()
    {
      axios( {
        method: "GET",
        url: "http://127.0.0.1:8000/api/group/members/list",
        params: {
          gid: this.group.gid,
          keyword: this.keyword
        }
      } ).then( ( result ) =>
      {
        if ( result.data.status )
        {
          this.Users = result.data.list; // 将后端数据赋值给 Users
          this.msg = result.data.msg;
        }
      } );
    },
    handleCurrentChange ( val )
    {
      console.log( `current page: ${ val }` );
    },
    handleDelete ( uid )
    {
      ElMessageBox.confirm( "是否确认踢出该成员", "Warning", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      } ).then( () =>
      {
        axios.post( "http://127.0.0.1:8000/api/group/members/remove", {
          uid: uid,
          gid: this.group.gid
        } ).then( response =>
        {
          ElMessage( {
            type: "success",
            message: "踢出成功",
          } );
          this.getData();
        } ).catch( error =>
        {
          ElMessage( {
            type: "error",
            message: "踢出失败，请重试",
          } );
        } );
      } ).catch( () =>
      {
        ElMessage( {
          type: "info",
          message: "你已取消操作",
        } );
      } );
    },
    handleSet ( user )
    {
      const type = user.type == "成员" ? 1 : 2;
      const msg = user.type == "成员" ? "是否将其设为管理员" : "是否取消其管理员权限";
      ElMessageBox.confirm( msg, {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      } ).then( () =>
      {
        axios.post( "http://127.0.0.1:8000/api/group/members/authority", {
          uid: user.uid,
          gid: this.group.gid,
          type: type
        } ).then( response =>
        {
          ElMessage( {
            type: "success",
            message: "操作成功",
          } );
          this.getData();
        } ).catch( error =>
        {
          ElMessage( {
            type: "error",
            message: "操作失败，请重试",
          } );
        } );
      } ).catch( () =>
      {
        ElMessage( {
          type: "info",
          message: "你已取消操作",
        } );
      } );
    },
    getAvatar ( user )
    {
      return user.pic;
    },
    getMyOpData ()
    {
      // console.log( "MyOp: " + this.gid )
      axios( {
        method: "GET",
        url: "http://127.0.0.1:8000/api/group/activity/statistic",
        params: {
          gid: this.gid
        }
      } ).then( response =>
      {
        for ( const key in response.data.data )
        {
          const item = {
            value: response.data.data[ key ],
            name: key
          };
          this.myOpData.push( item );
        }
        console.log( this.myOpData );
        if ( this.myOpData.length == 0 )
        {
          this.myOpData = [
            {
              value: 1,
              name: "暂无活动" // 如果是饼图，使用name字段
              // key: "该团队暂无举办活动~" // 如果是其他图表类型，可以使用key字段
            }
          ];
        }
        this.renderChart();
      } ).catch( error =>
      {
        console.error( "Error fetching data:", error );
      } );
    },
    renderChart ()
    {
      const chartDom = this.$refs.chart;
      const myChart = echarts.init( chartDom );
      // 使用从后端获取的数据更新图表配置
      this.option.series[ 0 ].data = this.myOpData;
      myChart.setOption( this.option );
    },

  },
  components: { GroupActivityCard }
};

</script>

<style scoped>
/* Adjustments for group information section */
.type {
  margin: 35px 0;
}

.custom-table {
  width: 100%;
}

.table-row {
  display: flex;
  border-bottom: 1px solid #ccc;
  width: 600px;
}

.header {
  font-weight: bold;
}

.table-cell {
  flex: 1;
  padding: 8px;
  align-items: center;
}


.common-layout {
  display: flex;
  max-width: 100%;
  max-height: 100%;
  margin: 20px;
  background-color: #e8e5ec;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.activity-layout {
  position: relative;
  z-index: 1;
}

.group-info {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.group-details {
  text-align: right;
}

.group_name {
  font-size: 23px;
  text-align: center;
}

.image.enlarged-image {
  width: 100%;
  /* 图片最大宽度 */
  height: auto;
  /* 自适应高度 */
  max-width: 100%;
  /* 图片最大宽度 */
  max-height: 100%;
  /* 图片最大高度 */
}

.group_name .enlarged-name {
  font-size: 28px;
  /* 调整字体大小 */
  font-weight: bold;
  /* 加粗字体 */
  margin-top: 10px;
  /* 可以根据需要调整上边距 */
}

.group-activity {
  display: flex;
  text-align: left;
  width: 100%;
  height: 100%;
  position: relative;
  z-index: 1;
}

/* Adjustments for navigation section */
.group-navigation {
  display: flex;
  flex-direction: column;
  margin-left: 100px;
  text-align: left;
}

.group-navigation h2 {
  font-size: 20px;
  margin-bottom: 10px;
  color: #333;
}

.group-navigation ul {
  cursor: pointer;
  list-style: none;
  padding: 0;
}

.group-navigation li {
  font-size: 16px;
  font-weight: bold;
  color: #666;
  margin-bottom: 10px;
}

.group-navigation a {
  text-decoration: none;
  color: #666;
  font-weight: bold;
  transition: color 0.3s ease;
}

.group-navigation a:hover {
  color: #333;
}

.group_instrudiction p {
  font-family: Arial, sans-serif;
  /* 修改字体 */
  font-size: 14px;
  /* 修改字体大小 */
  line-height: 1.5;
  /* 修改行高 */
  color: #555;
}

.custom-collapse-title {
  font-size: 16px;
  font-weight: bold;
  color: #666;
  border-radius: 10px;
  display: inline-block;
  /* 让标题内容成为一个块级元素 */
  cursor: pointer;
  /* 添加鼠标指针样式 */
}

.centered-aside {
  display: flex;
  justify-content: center;
  align-items: center;
}

.center-content {
  text-align: center;
}

.user-info {
  display: flex;
  align-items: center;
  margin: 23px;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 10px;
}

.button-container {
  display: flex;
  align-items: center;
  margin-top: 35px;
  /* 可以根据需要选择其他布局方式 */
}

.image {
  width: auto;
  height: auto;
  max-width: 100%;
  max-height: 100%;
}
</style>
