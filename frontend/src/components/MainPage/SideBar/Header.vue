<template>
  <div class="header">
    <!-- 左侧logo -->
    <div class="picLocation">
      <img src="../../../images/logo.png" class="pic" />
    </div>

    <div class="label">
      <BreadcrumbLabel />
    </div>

    <!-- 右侧内容 -->
    <div class="right">

      <el-badge v-if="nNum > 0" :value="nNum" class="item">
        <el-button type="primary" @click="table = true">查看通知</el-button>
      </el-badge>

      <div v-else class="item">
        <el-button type="primary" @click="table = true">查看通知</el-button>
      </div>

      <!-- 头像 -->
      <div>
        <el-avatar :size="50" :src="picture || './src/images/emptyAvatar.png'" />
      </div>

      <!-- 账号 -->
      <div class="text">
        <div class="textStyle">{{ name }}</div>
      </div>
    </div>
  </div>

  <el-drawer v-model="table" title="尚未查看的通知信息" direction="rtl" size="50%">
    <el-table :data="nList">
      <el-table-column property="time" label="通知时间" width="230" />
      <el-table-column property="text" label="通知内容" width="300" />
      <el-table-column label="操作">
        <template #default="scope">
          <el-button type="danger" plain @click="deleteRow(scope.$index, scope.row)">删除通知</el-button>
        </template>
      </el-table-column>
    </el-table>

    <div style="margin-top: 20px; text-align: center;">
      <el-button type="danger" @click="deleteAllNotifications">删除所有通知</el-button>
    </div>
  </el-drawer>
</template>

<script>
import { color } from "echarts/core"
import axios from 'axios'
export default {
  data ()
  {
    return {
      name: '',
      picture: '',
      nList: [],
      nNum: 0,

      table: false,
    };
  },
  methods: {
    deleteRow ( index, row )
    {
      let deleteRow = { nid: row.nid };
      axios( {
        method: "POST",
        url: "http://127.0.0.1:8000/api/notice/confirm",
        data: deleteRow,
      } ).then( ( result ) =>
      {
        console.log( result );
        if ( result.data.status )
        {
          this.nList.splice( index, 1 );
          this.nNum--;
        }
      } )
    },
    deleteAllNotifications ()
    {
      let deleteAll = { uid: JSON.parse( sessionStorage.getItem( "uid" ) ) };
      axios( {
        method: "POST",
        url: "http://127.0.0.1:8000/api/notice/confirm",
        data: deleteAll,
      } ).then( ( result ) =>
      {
        console.log( result );
        if ( result.data.status )
        {
          this.nList = [];
          this.nNum = 0;
        }
      } )
    }
  },
  created ()
  {
    axios( {
      method: "GET",
      url: "http://127.0.0.1:8000/api/user/information",
      params: {
        uid: JSON.parse( sessionStorage.getItem( "uid" ) ),
      },
    } ).then( ( result ) =>
    {
      if ( result.data.status )
      {
        this.name = result.data.info.name;
        this.picture = "http://127.0.0.1:8000" + result.data.info.picture;
      }
    } );

    axios( {
      method: "GET",
      url: "http://127.0.0.1:8000/api/notice/list",
      params: {
        uid: JSON.parse( sessionStorage.getItem( "uid" ) ),
      }
    } ).then( ( result ) =>
    {
      console.log( result );
      if ( result.data.status )
      {
        this.nList = result.data.list;  //nid, text, time
        this.nNum = result.data.list.length;
      }
    } )
  }
};
</script>

<style scoped>
.header {
  height: 100%;
  display: flex;
  justify-content: space-between;
  background-color: #5d85a6;
}

.item {
  margin-top: 10px;
  margin-right: 30px;
}

.picLocation {
  height: 90%;
  width: 100px;
  margin-top: 6px;
}

.label {
  display: flex;
  align-items: center;
  /* 让面包屑和右侧内容在垂直方向上居中对齐 */
  flex-grow: 1;
  /* 让父级容器撑满可用空间 */
  justify-content: space-between;
  /* 左右两侧分隔 */
}

.pic {
  background-repeat: no-repeat;
  background-position: center;
  object-fit: contain;
  width: 100%;
  height: 100%;
}

.right {
  margin-top: 6px;
  display: flex;
  flex-direction: row;
}

.text {
  display: flex;
  align-items: center;
  margin-left: 20px;
  margin-right: 20px;
}

.textStyle {
  font-size: 18px;
  color: white;
}</style>