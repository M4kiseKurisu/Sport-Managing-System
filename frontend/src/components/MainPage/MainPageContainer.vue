<template>
  <div class="common-layout">
    <el-container>
      <el-header>Header</el-header>
      <el-container>
        <el-aside width="200px">
          <Sidebar />
        </el-aside>
        <el-main>
          <!-- <UserInformation /> -->
          <GroupInformation />
          <!-- <EquipmentBorrow /> -->
          <FriendInformation />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>
  
<script>
// 引入 Sidebar 组件
import Sidebar from './SideBar/Sidebar.vue'; // 请替换为实际的路径
import UserInformation from './Page/UserInformation.vue';
import ActivityInformation from './Page/ActivityInformation.vue';
import EquipmentBorrow from './Page/EquipmentBorrow.vue'
import FriendInfomation from './Page/FriendInformation.vue';
import GroupInformation from './Page/GroupInformation.vue'

export default {
  components: {
    Sidebar,
    UserInformation,
    ActivityInformation,
    EquipmentBorrow,
    FriendInfomation
},
};
</script>