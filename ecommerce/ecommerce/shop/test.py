










# <!--{#		{% if cart.coupon %}
# 					<tr class="gray">
# 						<td>Subtotal</td>
# 						<td colspan="4"></td>
# 						<td class="num"> {{cart.get_total_price}}</td>
# 					</tr>
# 					<tr class="gray2">
# 						{% block trans   %}
# 							{% with code=cart.coupon.code discount=cart.coupon.discount%}
# 							    <td colspan="2">"{{code}}" coupon ({{discount}})% off</td>
# 							{% endwith %}
# 						{% endblock trans %}
# 						<td colspan="3"></td>
# 						<td class="num neg"> - ${{cart.get_discount|floatformat:"2"}}</td>
# 					</tr>
# 				{% endif %}
# 				<tr class="total">
# 					<td>Total</td>
# 					<td colspan="4"></td>
# 					<td class="num">${{cart.get_total_price_after_discount|floatformat:"2"}}</td>
# 				</tr>
# 		</tbody>
# 	</table>
# 	<div class="divo">
# 		<p>
# 			Apply a coupon
# 		</p>
# 		<form action="{% url 'coupons:apply' %}" method="post">
# 			{{coupon_apply_form}}
# 			{% csrf_token %}
# 			<input type="submit" value="apply" class="btn">
# 		</form>  #}-->
#
# 	<!--</div> -->







#
# {% if cart.coupon %}
# 					<li>
# 						"{{cart.coupon.code}}" ({{cart.coupon.discount}}% off)
# 						<span> - ${{cart.get_discount|floatformat:"2"}}</span>
# 					</li>
# 				{% endif %}