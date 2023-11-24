<template>
  <el-button @click="toggleCollapse" type="primary">
    <el-icon v-if="isCollapse">
      <MoreFilled />
    </el-icon>
    <el-icon v-else>
      <icon-menu />
    </el-icon>
  </el-button>
  <el-menu default-active="/Page/User_Information" class="el-menu-vertical-demo" :collapse="isCollapse" @open="handleOpen"
    @close="handleClose" router="true">

    <el-menu-item index="/Page/User_Information">
      <el-icon>
        <House />
      </el-icon>
      <template #title>
        用户主页
      </template>
    </el-menu-item>

    <el-menu-item index="/Page/Activity_Information">
      <el-icon><icon-menu /></el-icon>
      <template #title>活动列表</template>
    </el-menu-item>

    <el-menu-item index="/Page/GroupInformation">
      <el-icon>
        <Document />
      </el-icon>
      <template #title>团体信息</template>
    </el-menu-item>

    <el-menu-item index="4">
      <el-icon>
        <DocumentChecked />
      </el-icon>
      <template #title>你的活动</template>
    </el-menu-item>

    <el-menu-item index="/Page/Friend">
      <el-icon>
        <Connection />
      </el-icon>
      <template #title>好友列表</template>
    </el-menu-item>

    <el-menu-item index="/Page/Borrow_Equipment">
      <el-icon>
        <Discount />
      </el-icon>
      <template #title>器材租借</template>
    </el-menu-item>
  </el-menu>
</template>
   
<script lang="ts">
import { ref } from 'vue'
import {
  Search,
  Menu as IconMenu,
  Connection,
  ChatDotRound,
  House,
  MoreFilled,
  DocumentChecked,
  Avatar,
  Document,
  Discount
} from '@element-plus/icons-vue'


export default {

  components: {
    IconMenu,
    Search,
    Connection,
    ChatDotRound,
    House,
    MoreFilled,
    DocumentChecked,
    Avatar,
    Document,
    Discount
  },
  setup() {
    const moreFilledIcon = MoreFilled;
    const iconMenuIcon = IconMenu;

    const isCollapse = ref(true)
    const handleOpen = (key: string, keyPath: string[]) => {
      console.log(key, keyPath)
    }
    const handleClose = (key: string, keyPath: string[]) => {
      console.log(key, keyPath)
    }
    const toggleCollapse = () => {
      // 切换 isCollapse 的值
      isCollapse.value = !isCollapse.value
      // 在这里你可以执行其他与折叠状态切换相关的逻辑
      console.log('Collapse state changed. isCollapse:', isCollapse.value)
    }

    return {
      handleOpen,
      handleClose,
      isCollapse,
      toggleCollapse,
      moreFilledIcon,
      iconMenuIcon,
    };
  },
}
</script>
   
<style>
#sidebar {
  display: flex;
  flex-direction: column;
  /* 设置为垂直布局 */
}

.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 120px;
  min-height: 400px;
}
</style>
   