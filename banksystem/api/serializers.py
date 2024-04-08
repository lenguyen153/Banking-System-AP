from rest_framework import serializers

from .models import *

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('id', 'name','address','branch_code',)
        read_only_fields = ('id',)

class BankSerializer(serializers.ModelSerializer):
    branch_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Bank
        fields = ['id', 'name', 'branch_id']

    def create(self, validated_data):
        branch_id = validated_data.pop('branch_id')  # Extract branch_id from validated_data
        bank = Bank.objects.create(branch_id=branch_id, **validated_data)  # Create Bank instance with branch_id
        return bank

class BranchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('__all__')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('__all__')

class AccountSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    bank = BankSerializer()
    class Meta:
        model = Account
        fields = ('__all__')

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ('__all__')

class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = ('__all__')

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ('__all__')
