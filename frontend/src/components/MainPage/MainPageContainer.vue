<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <Header />
      </el-header>
      <el-container>
        <el-aside width="150px">
          <Sidebar />
        </el-aside>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>
  
<script>
// 引入 Sidebar 组件
import Header from "./SideBar/Header.vue";
import Sidebar from "./SideBar/Sidebar.vue"; // 请替换为实际的路径
import UserInformation from "./Page/UserInformation.vue";
// import ActivityInformation from "./Page/ActivityInformation.vue";
import EquipmentBorrow from "./Page/EquipmentBorrow.vue";
import EBorrowMain from "./Page/E-Borrow/EBorrowMain.vue";
import FriendInformation from "./Page/FriendInformation.vue";
import GroupInformation from "./Page/GroupInformation.vue";
import Details from "./Page/Group/Details.vue";
// import BreadcrumbLabel from "./Components/BreadcrumbLabel.vue";
// import UploadMoment from "./Page/Moments/UploadMoment.vue";
//import CreateGroup from "./Components/CreateGroup.vue";

export default {
  components: {
    Header,
    Sidebar,
    UserInformation,
    // ActivityInformation,
    EquipmentBorrow,
    EBorrowMain,
    FriendInformation,
    GroupInformation,
    UserInformation,
    Details,
    // BreadcrumbLabel
  },
};
</script>

<style scoped>
.el-header {
  --el-header-padding: 0;
}
</style>