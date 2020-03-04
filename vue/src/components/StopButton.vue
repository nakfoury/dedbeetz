<template>
  <b-button
    pill
    size="lg"
    style="padding: 12px 28px 12px 24px"
    @click="$emit('click')"
  >
    <b-icon-stop-fill />
    Stop
  </b-button>
</template>

<script>
import { BIconStopFill } from 'bootstrap-vue';

export default {
  components: { BIconStopFill },
};
</script>
