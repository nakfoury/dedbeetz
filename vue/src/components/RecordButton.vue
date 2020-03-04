<template>
  <b-button
    variant="danger"
    pill
    size="lg"
    style="padding: 12px 28px 12px 24px"
    @click="$emit('click')"
  >
    <b-icon-circle-fill />
    Record
  </b-button>
</template>

<script>
import { BIconCircleFill } from 'bootstrap-vue';

export default {
  components: { BIconCircleFill },
};
</script>
