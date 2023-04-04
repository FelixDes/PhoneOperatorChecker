<template>
    <v-container class="fill-height">
        <v-app-bar :elevation="2">
            <v-app-bar-title class="text-center">Phone operator checker</v-app-bar-title>
        </v-app-bar>
        <v-responsive class="d-flex text-center fill-height">
            <v-col class="mt-10">
                <span class="align-start">Paste your phone number</span>
                <v-text-field :rules="rules" v-model="phone"></v-text-field>
                <v-btn @click="submit">
                    Get provider
                </v-btn>
                <v-divider vertical v-if="resShow"></v-divider>
                <v-card v-if="resShow" class="mt-4 pa-3">
                    <span>{{ provider }}</span>
                </v-card>
            </v-col>
        </v-responsive>
    </v-container>
</template>

<script>

import axios from "axios"

export default {
    name: "PhoneChecker",
    data() {
        return {
            phone: null,
            resShow: false,
            provider: '',
            rules: [
                value => !!value || 'Required.',
                value => {
                    const pattern = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/
                    return pattern.test(value) || 'Invalid phone number.'
                },
            ],
        }
    },
    methods: {
        submit() {
            axios.get("http://127.0.0.1:5000/?phoneNumber=" + this.preparePhone(this.phone), {
                    "Access-Control-Allow-Origin": "*",
                    'Access-Control-Allow-Credentials': true,
                }
            ).then((res) => {
                this.resShow = true
                this.provider = res.data
            })
        },
        preparePhone(phoneNumber) {
            let pn = String(phoneNumber);
            pn=pn.substring(1)
            return pn;
        }
    }
}
</script>

<style scoped>

</style>
