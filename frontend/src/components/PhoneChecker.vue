<template>
  <v-container class="fill-height">
    <v-app-bar :elevation="2">
      <v-app-bar-title class="text-center">Phone operator checker</v-app-bar-title>
    </v-app-bar>
    <v-responsive class="d-flex align-center text-center fill-height">
      <v-row>
        <v-col>
          <v-text-field
            :value="currentValue"
            return-masked-value
            mask="+7.###.###.##-##"
            @input="handleInput"
          ></v-text-field>
          <v-btn>

          </v-btn>
        </v-col>
        <v-divider vertical></v-divider>
        <v-col></v-col>
      </v-row>
    </v-responsive>
  </v-container>
</template>

<script setup lang="ts">
</script>
