<template>
    <v-container class="fill-height">
        <v-app-bar :elevation="2">
            <v-app-bar-title class="text-center">Phone operator checker</v-app-bar-title>
        </v-app-bar>
        <v-responsive class="d-flex text-center fill-height">
            <v-col class="mt-10">
                <span class="align-start">Paste your phone number</span>
                <vue-tel-input @input="preparePhone"></vue-tel-input>
                <v-btn @click="submit">
                    Get provider
                </v-btn>
                <v-divider vertical v-if="resShow"></v-divider>
                <v-card v-if="resShow" class="d-flex mt-4 pa-3 flex-column">
                    <span>{{ provider }}</span>
                    <span>{{ region }}</span>
                </v-card>
            </v-col>
        </v-responsive>
    </v-container>
</template>

<script>
import {VueTelInput} from 'vue3-tel-input'
import 'vue3-tel-input/dist/vue3-tel-input.css'

export default {
    name: "PhoneChecker",
    components: {
        VueTelInput,
    },
    data() {
        return {
            phone: null,
            resShow: false,
            provider: '',
            region: '',
        }
    },
    methods: {
        submit() {
            this.$root.doGet("/?phoneNumber=" + this.preparePhone(this.phone), {
                "Access-Control-Allow-Origin": "*",
                'Access-Control-Allow-Credentials': true,
            }).then((res) => {
                console.log(res)
                this.resShow = true
                this.provider = res.provider
                this.region = res.region
            })
        },
        preparePhone(phone, phoneObject) {
            if (phoneObject?.formatted) {
                this.phone = phoneObject.nationalNumber
            }
            // console.log(phone + " | " + JSON.stringify(phoneObject))

        }
    }
}
</script>

<style scoped>

</style>
