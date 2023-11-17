<template>
    <div>
        <div class="form">
            <el-table :data="tableData" style="width: 100%">
                <el-table-column prop="column1" label="器材类型"></el-table-column>
                <el-table-column prop="column2" label="剩余数量"></el-table-column>
                <el-table-column label="申请器材">
                    <template #default="{ row }">
                        <el-button type="primary" @click="handleClick(row)">申请此器材</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </div>

        <div class="title">器材申请</div>

        <div class="apply">
            <el-form :model="form" ref="form" label-width="120px" style="width: 800px" :inline="true">

                <el-form-item label="器材类型">
                    <el-select v-model="form.equipmentType" :placeholder="fyb">
                        <el-option v-for="item in equipmentTypes" :key="item.value" :label="item.label" :value="item.value">
                        </el-option>
                    </el-select>
                </el-form-item>

                <br>

                <el-form-item label="申请者类型">
                    <el-radio-group v-model="form.applicantType">
                        <el-radio :label="'personal'">个人</el-radio>
                        <el-radio :label="'group'">团体</el-radio>
                    </el-radio-group>
                </el-form-item>

                <el-form-item label="ID">
                    <el-input v-model="form.id" style="width: 100px"></el-input>
                </el-form-item>

                <el-form-item label="开始时间">
                    <el-date-picker v-model="form.startTime" type="datetime" placeholder="选择开始时间">
                    </el-date-picker>
                </el-form-item>

                <br>

                <el-form-item label="结束时间">
                    <el-date-picker v-model="form.endTime" type="datetime" placeholder="选择结束时间">
                    </el-date-picker>
                </el-form-item>

                <br>

                <el-form-item label="器材数量">
                    <el-input-number v-model="form.quantity" :min="1"></el-input-number>
                </el-form-item>

                <br>

                <el-form-item style="margin-left: 60px; margin-top: 10px;">
                    <el-button type="primary" @click="submitForm('form')">立即申请</el-button>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>
  
<script>
export default {
    data() {
        return {
            tableData: [
                { column1: '篮球', column2: 21 },
                { column1: '足球', column2: 24 },
                { column1: '飞盘', column2: 8 },
                { column1: '乒乓球', column2: 32 },
                { column1: '羽毛球', column2: 13 },
                { column1: '软式排球', column2: 3 },
                { column1: '气排球', column2: 6 },
                { column1: '网球', column2: 36 },
            ],
            form: {
                equipmentType: '',
                applicantType: '',
                id: '',
                startTime: '',
                endTime: '',
                quantity: 1
            },
            equipmentTypes: [
                { value: 'type1', label: '篮球' },
                { value: 'type2', label: '足球' },
                { value: 'type3', label: '飞盘' },
                { value: 'type4', label: '乒乓球' },
                { value: 'type5', label: '羽毛球' },
                { value: 'type6', label: '软式排球' },
                { value: 'type7', label: '气排球' },
                { value: 'type8', label: '网球' },
            ],
            fyb: "请选择器材类型"
        }
    },
    methods: {
        submitForm(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    alert('submit!');
                    // 此处应添加提交表单的代码
                } else {
                    console.log('error submit!!');
                    return false;
                }
            });
        },
        handleClick(row) {
            console.log(row.column1)
            this.fyb = row.column1
        }
    }
}
</script>

<style scoped>
.form {
    display: flex;
}

.title {
    margin-top: 30px;
    font-size: 18px;
}

.apply {
    display: flex;
    margin-top: 30px;
}
</style>