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
          <!-- <ActivityInformation /> -->
          <!-- <GroupInformation /> -->
          <!-- <EquipmentBorrow />  -->

          <!-- <UserInformation /> -->
          <!-- <ActivityInformation /> -->
          <!-- <GroupInformation /> -->
          <!-- <EquipmentBorrow /> -->

          <!-- <EBorrowMain /> -->
          <!-- <GroupInformation /> -->
          <router-view></router-view>
          <!-- <FriendInformation /> -->
          <!-- <GroupMainPage /> -->
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
import EBorrowMain from './Page/E-Borrow/EBorrowMain.vue'
import FriendInformation from './Page/FriendInformation.vue';
import GroupInformation from './Page/GroupInformation.vue'
import GroupMainPage from './Page/Group/GroupMainPage.vue';


export default {
  components: {
    Sidebar,
    UserInformation,
    ActivityInformation,
    EquipmentBorrow,
    EBorrowMain,
    FriendInformation,
    GroupInformation,
    UserInformation,
    GroupMainPage
},
};
</script>