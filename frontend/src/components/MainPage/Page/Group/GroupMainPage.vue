<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="200px" class="centered-aside">
        <div class="group-info">
          <!-- Left section for group information -->
          <div class="group-details">
            <div class="center-content">
              <img :src="group.image" alt="group Image" class="group-image" />
              <div class="group_name">
                <h1>{{ group.name }}</h1>
              </div>
            </div>
          </div>
        </div>
      </el-aside>
      <el-main width="20%">
        <div class="group-navigation">
          <!-- Right section for navigation -->
          <el-card>
            <el-collapse v-model="activeName" accordion>
              <el-collapse-item name="1" class="group_instrudiction">
                <template #title class = "collapse_title">
                  <span class="custom-collapse-title">团队简介</span>
                </template>
                <p>{{ group.description }}</p>
              </el-collapse-item>
            </el-collapse>
          </el-card>
          <ul>
            <el-card><li><a href="#activities">团队活动</a></li></el-card>
            <el-card><li><a href="#equipment">团队器材</a></li></el-card>
            <el-card><li><a href="#members">团队成员</a></li></el-card>
            <!-- Add more navigation links as needed -->
          </ul>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      group: {
        image: './src/images/group-default-picture.png', // Replace with your group image path
        name: '团队名称',
        description: '团队简介描述'
      }
    };
  }
};
</script>

<style scoped>
/* Adjustments for group information section */
.common-layout {
  display: flex;
  max-width: 80%;
  max-height: 100%;
  margin: 20px;
  background-color: #f1e9fd;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.group-info {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.group-details {
  text-align: right;
}
.group_name{
  font-size: 23px;
  text-align: center;
}
.group-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px; /* Added border-radius */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
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
  list-style: none;
  padding: 0;
}

.group-navigation li {
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

.group_instrudiction p{
  font-family: Arial, sans-serif; /* 修改字体 */
  font-size: 14px; /* 修改字体大小 */
  line-height: 1.5; /* 修改行高 */
  color: #555;
}

.custom-collapse-title {
  font-size: 16px;
  font-weight: bold;
  color: #666;
  border-radius: 10px;
  display: inline-block; /* 让标题内容成为一个块级元素 */
  cursor: pointer; /* 添加鼠标指针样式 */
}

.centered-aside {
  display: flex;
  justify-content: center;
  align-items: center;
}

.center-content {
  text-align: center;
}
</style>
