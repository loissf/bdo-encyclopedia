<template>
  <div class="orders">
    <div class="header">
      <span>Sellers</span>
      <span>Prices</span>
      <span>Buyers</span>
    </div>
    <ul>
      <li
        v-for="(order, index) in data"
        :key="index"
        class="order-item"
        :class="order.sell ? 'sell' : 'buy'"
      >
        <span class="price" :class="getPriceColor(order.price)">{{
          order.price
        }}</span>
        <span class="orders">
          <span v-if="order.orders > 0"
            >{{ order.sell ? "Listed: " : "Orders: " }} {{ order.orders }}</span
          >
        </span>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { useMarketStore } from "@/components/market-store";
import { ItemOrders } from "@/models/Item";
import { getItemOrders } from "@/queries";
import { computed, ref } from "vue";
const marketStore = useMarketStore();

const basePrice = computed(
  () => marketStore.selectedEnhancement?.basePrice ?? 0
);

function getPriceColor(price: number) {
  if (price > basePrice.value) {
    return "overpriced";
  } else if (basePrice.value > price) {
    return "underpriced";
  }
}

const data = ref<ItemOrders[]>([]);

if (marketStore.selectedEnhancement) {
  getItemOrders(
    marketStore.selectedEnhancement.id,
    marketStore.selectedEnhancement.enhancement
  ).then((result) => {
    if (result.length > 1) {
      const priceInterval = result[0].price - result[1].price;

      const items = Array<ItemOrders>();

      let j = 0;
      for (
        let i = result[0].price;
        i >= result[result.length - 1].price;
        i -= priceInterval
      ) {
        if (result[j].price >= i) {
          items.push(result[j]);
          j++;
        } else {
          items.push({
            price: i,
            orders: 0,
            sell: result[j].sell,
          });
        }
      }

      data.value = items;
    } else {
      // Math.pow(10, result[0].price.toString().length);

      data.value = result;
    }
  });
}
</script>

<style scoped lang="scss">
.orders {
  width: 25rem;

  .header {
    display: flex;
    flex-direction: row;

    align-items: center;
    justify-content: space-around;

    font-size: 80%;

    border-radius: 4px;
    margin: 0.5rem;
    background-color: rgb(112, 112, 112);

    span {
      padding: 0.5rem;
    }
  }

  .order-item {
    display: flex;

    align-items: center;
    justify-content: center;

    &.sell {
      background-color: rgba(65, 110, 146, 0.75);
      flex-direction: row-reverse;
    }

    &.buy {
      background-color: rgba(119, 55, 60, 0.75);
      flex-direction: row;
    }

    &::before {
      flex: 1;
      content: "";
    }

    .price {
      padding: 0.375rem;

      &.overpriced {
        color: rgb(226, 47, 62);
      }

      &.underpriced {
        color: rgb(151, 198, 236);
      }
    }

    .orders {
      flex: 1;
      font-size: 80%;
      color: rgba(196, 196, 196, 0.75);
    }
  }

  ul {
    padding: 0;
    margin: 0.5rem;

    li {
      display: block;
      width: 100%;

      border-radius: 4px;

      &:not(:last-child) {
        margin-bottom: 0.375rem;
      }

      &:hover {
        filter: brightness(90%);
      }
    }
  }
}
</style>
